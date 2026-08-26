<div align="center">

<br/>

<table width="100%">
  <tr>
    <td align="center" style="background-color: #2D1B6E; padding: 40px 20px; border-radius: 16px;">
      <img src="https://api.iconify.design/ph/game-controller-fill.svg?color=%23F4B8D4&height=48" height="48" alt="Game Controller Icon" />
      <h1 style="color: #FDFBF7; font-size: 32px; letter-spacing: 3px; margin: 15px 0 5px 0; border: none;">CONECTA 4 MULTIPLAYER</h1>
      <p style="color: #F4B8D4; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; margin: 0 0 15px 0;">Real-Time WebSockets & AI Opponent</p>
      <p style="color: #FDFBF7; font-size: 15px; max-width: 550px; margin: 0 auto; line-height: 1.5; opacity: 0.9;">
        Juego multijugador en tiempo real con WebSockets, oponente IA vía Groq LLM y una estética pixel-art pastel inspirada en las tarjetas de memoria de los videojuegos retro.
      </p>
    </td>
  </tr>
</table>

<br/>

![Kawaii Pixel Art](https://img.shields.io/badge/kawaii_pixel_art-c5b9f0?style=for-the-badge&logoColor=2d1b6e)
![Real-Time WebSockets](https://img.shields.io/badge/real--time_websockets-f4b8d4?style=for-the-badge&logoColor=2d1b6e)
![AI Opponent](https://img.shields.io/badge/AI_opponent-b8e8d4?style=for-the-badge&logoColor=2d1b6e)

<br/>

<a href="https://conecta4-frontend.onrender.com">
  <img src="https://img.shields.io/badge/DEMO_EN_VIVO-5F6B56?style=for-the-badge&logo=googlechrome&logoColor=FDFBF7" alt="Demo en vivo" />
</a>
&nbsp;
<a href="https://conecta4-backend.onrender.com">
  <img src="https://img.shields.io/badge/BACKEND_API-A8C4F0?style=for-the-badge&logo=fastapi&logoColor=2d1b6e" alt="Backend API" />
</a>
&nbsp;
<a href="https://github.com/mee96/juego-conecta-4">
  <img src="https://img.shields.io/badge/REPOSITORIO-D49A99?style=for-the-badge&logo=github&logoColor=333333" alt="GitHub Repo" />
</a>

</div>

<br/>

---

## <img src="https://api.iconify.design/ph/sparkle-fill.svg?color=%232D1B6E&height=22" height="20"> &nbsp;Funcionalidades

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 style="color: #2D1B6E; margin-top: 0;">
        <img src="https://api.iconify.design/ph/users-three-fill.svg?color=%232D1B6E&height=20" height="18" /> &nbsp;PvP en tiempo real
      </h3>
      <p>Dos jugadores se conectan al mismo código de sala y juegan en vivo con sincronización vía WebSockets.</p>
    </td>
    <td width="50%" valign="top">
      <h3 style="color: #2D1B6E; margin-top: 0;">
        <img src="https://api.iconify.design/ph/robot-fill.svg?color=%232D1B6E&height=20" height="18" /> &nbsp;Oponente IA
      </h3>
      <p>En partidas individuales, el servidor activa una IA impulsada por el modelo <code>llama-3.1-8b-instant</code> de Groq.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3 style="color: #2D1B6E; margin-top: 0;">
        <img src="https://api.iconify.design/ph/user-minus-fill.svg?color=%232D1B6E&height=20" height="18" /> &nbsp;Sin registro
      </h3>
      <p>Acceso directo indicando únicamente un nombre de usuario y un código de sala.</p>
    </td>
    <td width="50%" valign="top">
      <h3 style="color: #2D1B6E; margin-top: 0;">
        <img src="https://api.iconify.design/ph/device-mobile-fill.svg?color=%232D1B6E&height=20" height="18" /> &nbsp;Diseño Responsive & UI Pixel-Art
      </h3>
      <p>Optimizada para escritorio y móvil con toque directo en columna, tipografía retro Press Start 2P y estética pastel.</p>
    </td>
  </tr>
</table>

<br/>

---

## <img src="https://api.iconify.design/ph/code-bold.svg?color=%232D1B6E&height=22" height="20"> &nbsp;Stack tecnológico

### Frontend

![Angular](https://img.shields.io/badge/Angular_19-c5b9f0?style=for-the-badge&logo=angular&logoColor=2d1b6e)
![TypeScript](https://img.shields.io/badge/TypeScript-b8e8d4?style=for-the-badge&logo=typescript&logoColor=2d1b6e)
![WebSocket](https://img.shields.io/badge/WebSocket-f4b8d4?style=for-the-badge&logo=socketdotio&logoColor=2d1b6e)
![CSS3](https://img.shields.io/badge/CSS3-f0e4a0?style=for-the-badge&logo=css3&logoColor=2d1b6e)
![Render](https://img.shields.io/badge/Render-a8c4f0?style=for-the-badge&logo=render&logoColor=2d1b6e)

### Backend

![FastAPI](https://img.shields.io/badge/FastAPI-b8e8d4?style=for-the-badge&logo=fastapi&logoColor=2d1b6e)
![Python](https://img.shields.io/badge/Python-c5b9f0?style=for-the-badge&logo=python&logoColor=2d1b6e)
![Groq](https://img.shields.io/badge/Groq_LLM-f4b8d4?style=for-the-badge&logo=groq&logoColor=2d1b6e)
![Uvicorn](https://img.shields.io/badge/Uvicorn-f0e4a0?style=for-the-badge&logo=gunicorn&logoColor=2d1b6e)
![Render](https://img.shields.io/badge/Render-a8c4f0?style=for-the-badge&logo=render&logoColor=2d1b6e)

<br/>

---

## <img src="https://api.iconify.design/ph/tree-structure-fill.svg?color=%232D1B6E&height=22" height="20"> &nbsp;Arquitectura

```text
┌─────────────────────────────────────────────────────────┐
│                         CLIENTE                         │
│                                                         │
│  LoginComponent  ──►  WebsocketService  ──►  GameComponent │
│  (sala + nombre)      (signals estado)     (tablero 6×7) │
└───────────────────────────┬─────────────────────────────┘
                            │  WebSocket (wss://)
┌───────────────────────────▼─────────────────────────────┐
│                        SERVIDOR                         │
│                                                         │
│  FastAPI /ws  ──►  ConnectionManager  ──►  GameManager  │
│                    (salas/jugadores)    (lógica/victoria)│
│                            │                            │
│                            ▼                            │
│                        Groq SDK                         │
│                  (movimiento IA si 1 jugador)           │
└─────────────────────────────────────────────────────────┘
```

### Protocolo de mensajes WebSocket

```typescript
// Cliente → Servidor
{ type: 'join',        payload: { name: string, room: string } }
{ type: 'move',        payload: { column: number } }
{ type: 'play_vs_ai', payload: {} }

// Servidor → Cliente
{ type: 'state',         payload: { board, currentTurn, players, isAiGame } }
{ type: 'winner',        payload: { winner: 'P1' | 'P2' | 'draw' } }
{ type: 'wait',          payload: { message: string } }
{ type: 'opponent_left', payload: {} }
{ type: 'error',         payload: { message: string } }
```

<br/>

---

## <img src="https://api.iconify.design/ph/arrows-merge-bold.svg?color=%232D1B6E&height=22" height="20"> &nbsp;Flujo del juego

```text
Introduce nombre + código de sala
              │
              ▼
       Pantalla de espera
       ┌──────┴──────┐
       │             │
 llega rival   "Jugar contra IA"
    humano           │
       │             │
       └──────┬──────┘
              ▼
       Partida iniciada
              │
       ┌──────┴──────┐
       │             │
      PvP          vs IA
 (2 pestañas)    (Groq LLM)
              │
              ▼
       Victoria / Empate
              │
              ▼
     Volver a jugar / Menú
```

<br/>

---

## <img src="https://api.iconify.design/ph/folder-fill.svg?color=%232D1B6E&height=22" height="20"> &nbsp;Estructura del proyecto

```text
juego-conecta-4/
├── frontend/
│   └── src/
│       ├── app/
│       │   ├── models/
│       │   │   └── game.ts         # Interfaces y tipos TypeScript
│       │   ├── services/
│       │   │   └── websocket.ts   # WebSocket + estado con signals
│       │   ├── login/
│       │   │   ├── login.ts
│       │   │   ├── login.html
│       │   │   └── login.css
│       │   ├── game/
│       │   │   ├── game.ts
│       │   │   ├── game.html
│       │   │   └── game.css
│       │   ├── app.ts
│       │   ├── app.html
│       │   └── app.config.ts
│       ├── styles.css             # Tokens globales y tema pixel-art
│       └── index.html
└── backend/
    ├── main.py                    # App FastAPI + endpoint WebSocket
    ├── connection_manager.py      # Gestión de salas y jugadores
    ├── game_manager.py            # Lógica del tablero y detección de victoria
    ├── ai_player.py               # Integración Groq SDK
    └── requirements.txt
```

<br/>

---

## <img src="https://api.iconify.design/ph/terminal-window-fill.svg?color=%232D1B6E&height=22" height="20"> &nbsp;Ejecutar en local

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts ctivate
pip install -r requirements.txt

# Crear fichero .env
echo "GROQ_API_KEY=tu_key_aqui" > .env

uvicorn main:app --reload
# Servidor en http://localhost:8000
```

### Frontend

```bash
cd frontend
npm install
ng serve
# App en http://localhost:4200
```

> **Nota:** asegúrate de que el backend esté corriendo antes de abrir el frontend. Consigue una API key gratuita de Groq en [console.groq.com](https://console.groq.com).

<br/>

---

## <img src="https://api.iconify.design/ph/cloud-arrow-up-fill.svg?color=%232D1B6E&height=22" height="20"> &nbsp;Despliegue

| Servicio | Plataforma | Configuración |
| :--- | :--- | :--- |
| **Backend** | Render Web Service | Root dir: `backend` · Start: `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| **Frontend** | Render Static Site | Root dir: `frontend` · Build: `npm install && ng build` · Publish: `dist/frontend/browser` |

Variables de entorno configuradas en el dashboard de Render (nunca en git):
* `GROQ_API_KEY`

<br/>

---

## <img src="https://api.iconify.design/ph/lightbulb-fill.svg?color=%232D1B6E&height=22" height="20"> &nbsp;Lo que he aprendido

* Implementar **comunicación bidireccional en tiempo real** con WebSockets tanto en FastAPI (async) como en Angular.
* Gestionar el **estado reactivo de la UI** exclusivamente con Angular Signals (sin RxJS ni NgRx).
* Integrar un **LLM como oponente de juego** vía Groq SDK con un prompt estructurado que devuelve un único número de columna.
* Diseñar un **sistema multijugador basado en salas** donde el servidor detecta el número de jugadores y cambia dinámicamente entre modo PvP y modo IA.
* Desplegar una **aplicación WebSocket full-stack** en Render, gestionando `ws://` → `wss://` y configuración de CORS.

<br/>

---

<div align="center">

Desenvolupat per **Carme Medina Canalda**  
*Full Stack Developer · Barcelona*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-2D1B6E?style=flat-square&logo=linkedin&logoColor=FDFBF7)](https://www.linkedin.com/in/carme-medina-canalda-250457132/)
[![Portfolio](https://img.shields.io/badge/Portfolio-D49A99?style=flat-square&logoColor=333333)](https://carme-portfoli.onrender.com/)

</div>
