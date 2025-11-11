import { useEffect, useState } from 'react'

import './App.css'

function App() {
  const [showNotification, setShowNotification] = useState(false);
  const [notifications, setNotifications] = useState([])
  useEffect(()=>{
    const ws = new WebSocket("ws://localhost:8000/ws/notifications/admin/");
    ws.onopen = () => {
      console.log("Web socket connected");
    }

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data)
      console.log("Received: ", data);

      if (data.type === "product_created"){
        setShowNotification(true)
        console.log("Product Created Notification Received: ", data.data)
        setNotifications(prevNotifs => Array.from(new Set([...prevNotifs, data.data.message])))
      }
    }

    ws.onerror = (error) => {
      console.log("Websocket Error: ", error)
    }

    ws.onclose = () => {
      console.log("Websocket disconnected")
    }

  }, [])
  return (
    <>
      <h1> Notifications </h1>
      { showNotification && 

        <ul>
          {
            notifications.map((notif, index) => {
              return <li key={index}>
                {notif}
              </li>
            })
          }
      </ul>
      }
    </>
  )
}

export default App
