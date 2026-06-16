import os
import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from connection_manager import ConnectionManager, Player
from game_manager import drop_piece, check_winner, is_draw
from ai_player import get_ai_move

load_dotenv()

app = FastAPI(title="Conecta 4 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = ConnectionManager()

AI_THINK_DELAY = 0.8  # segons que "pensa" la IA


@app.get("/")
async def health():
    return {"status": "ok", "game": "Conecta 4"}


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    room_id: str | None = None

    try:
        # ── 1. Espera missatge join ──────────────────────────
        raw = await ws.receive_json()

        if raw.get("type") != "join":
            await ws.send_json({
                "type": "error",
                "payload": {"message": "Primer cal fer join."}
            })
            await ws.close()
            return

        name    = str(raw["payload"]["name"]).strip()[:16] or "Anònim"
        room_id = str(raw["payload"]["room"]).strip()[:12] or "default"

        # ── 2. Entra a la sala ───────────────────────────────
        room = manager.get_or_create_room(room_id)

        if room.is_full():
            await ws.send_json({
                "type": "error",
                "payload": {"message": "La sala és plena."}
            })
            await ws.close()
            return

        color = "P1" if not room.players else "P2"
        player = Player(ws=ws, name=name, color=color)
        room.players.append(player)

        # ── 3. Lògica d'espera ───────────────────────────────
        if len(room.players) == 1:
            # Primer jugador: espera que passi alguna cosa
            await ws.send_json({
                "type": "wait",
                "payload": {"message": f"Esperant rival a la sala '{room_id}'..."}
            })

            # Bucle d'espera: rival humà O botó play_vs_ai
            while len(room.players) == 1 and not room.is_ai_game:
                try:
                    msg = await asyncio.wait_for(ws.receive_json(), timeout=1.0)
                    if msg.get("type") == "play_vs_ai":
                        room.is_ai_game = True
                        room.players.append(
                            Player(ws=ws, name="IA ✦", color="P2")
                        )
                except asyncio.TimeoutError:
                    pass  # segueix esperant

        # ── 4. Inicia la partida ─────────────────────────────
        await manager.broadcast(room, {
            "type": "state",
            "payload": room.state_payload(),
        })

        # ── 5. Bucle principal de joc ────────────────────────
        while not room.finished:
            data = await ws.receive_json()

            if data.get("type") != "move":
                continue

            current_player = room.get_player_by_ws(ws)
            if current_player is None:
                continue

            if room.current_turn != current_player.color:
                await manager.send_to(ws, {
                    "type": "error",
                    "payload": {"message": "No és el teu torn."}
                })
                continue

            col = int(data["payload"]["column"])
            if col < 0 or col > 6:
                continue

            # Aplica el moviment
            row = drop_piece(room.board, col, current_player.color)
            if row is None:
                await manager.send_to(ws, {
                    "type": "error",
                    "payload": {"message": "Columna plena."}
                })
                continue

            # Comprova victòria o empat
            winner = check_winner(room.board, row, col)
            if winner:
                room.finished = True
                await manager.broadcast(room, {
                    "type": "winner",
                    "payload": {"winner": winner}
                })
                break

            if is_draw(room.board):
                room.finished = True
                await manager.broadcast(room, {
                    "type": "winner",
                    "payload": {"winner": "draw"}
                })
                break

            # Canvia torn i envia estat
            room.current_turn = "P2" if room.current_turn == "P1" else "P1"
            await manager.broadcast(room, {
                "type": "state",
                "payload": room.state_payload(),
            })

            # ── 6. Torn de la IA ─────────────────────────────
            if room.is_ai_game and room.current_turn == "P2" and not room.finished:
                await asyncio.sleep(AI_THINK_DELAY)

                ai_col = await get_ai_move(room.board)
                ai_row = drop_piece(room.board, ai_col, "P2")

                if ai_row is not None:
                    winner = check_winner(room.board, ai_row, ai_col)
                    if winner:
                        room.finished = True
                        await manager.broadcast(room, {
                            "type": "winner",
                            "payload": {"winner": winner}
                        })
                        break

                    if is_draw(room.board):
                        room.finished = True
                        await manager.broadcast(room, {
                            "type": "winner",
                            "payload": {"winner": "draw"}
                        })
                        break

                    room.current_turn = "P1"
                    await manager.broadcast(room, {
                        "type": "state",
                        "payload": room.state_payload(),
                    })

    except WebSocketDisconnect:
        pass
    except Exception as e:
        print(f"[WS error] {e}")
    finally:
        if room_id:
            await manager.disconnect(ws, room_id)