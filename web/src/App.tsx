import { useEffect } from 'react'
import { io } from 'socket.io-client'


export default function App() {
useEffect(() => {
const s = io('/rt')
s.on('presence', (msg) => console.log('presence:', msg))
return () => { s.disconnect() }
}, [])
return (
<div style={{fontFamily:'system-ui', padding:16}}>
<h1>Factura RT – Demo Pública</h1>
<p>Scaffold inicial. Próximamente: Login, clientes, facturas, dashboard.</p>
<ul>
<li>Backend: <code>/api</code> (FastAPI)</li>
<li>WebSockets: <code>/rt</code> (Socket.IO)</li>
<li>Frontend: React + Vite</li>
</ul>
</div>
)
}