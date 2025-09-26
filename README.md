# Factura RT — Demo pública


Sistema de control de facturas con stack moderno (FastAPI + React/Vite), preparado para tiempo real (Socket.IO) y despliegue en Docker.  

## Stack

- **FastAPI** (Python 3.11), **SQLAlchemy** / Alembic  
- **PostgreSQL**, **Redis**  
- **Socket.IO** (ASGI)  
- **React + Vite**  
- **Caddy** (reverse proxy)  
- **Docker Compose**


 
**Este repo es público y no contiene datos reales ni secretos.**

> **Estado del demo:** Scaffold funcional.  
> - Backend: endpoint de salud y Socket.IO montado.  
> - Frontend: Vite listo para build estática.  
> - Proxy: Caddy sirve el frontend y hace reverse-proxy a la API.

---

## Arquitectura (resumen)

┌───────────┐ /api/* → reverse_proxy → http://api:8000

│ Caddy │ / → archivos estáticos de web (dist)
└─────┬─────┘
│
▼
┌───────────┐ ┌────────────┐
│ web │ │ api │──► PostgreSQL (db)
│ (Vite) │ │ (FastAPI) │──► Redis
└───────────┘ └────────────┘
---

- **Caddy** (puerto 80):  
  - `GET /` → sirve `web/dist/`  
  - `GET /ping` → responde `ok` (sanity-check del proxy)  
  - `GET /api/*` → redirige hacia `api:8000`

- **API** (puerto 8000 expuesto):  
  - `GET /api/health` → `{ "status": "ok" }`
  - WebSockets en `/rt` (Socket.IO) — placeholder para tiempo real.

---

## Requisitos

- Docker Desktop (o Docker + Docker Compose)
- (Opcional) Python 3.11 y Node 18/20 si quieres trabajar fuera de Docker

---

## Arranque rápido (desarrollo)
1. Copia `.env.sample` a `.env` y ajusta valores *de prueba*.
2. `docker compose -f docker/compose.yml up -d --build`
3. (Próximamente) `docker compose exec api alembic upgrade head`
4. Abre `http://localhost` → verás el frontend. `http://localhost/api/health` → API OK.
