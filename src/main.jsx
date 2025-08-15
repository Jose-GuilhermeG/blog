import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Main_Routes from './routes'

createRoot(document.getElementById('root')).render(
  <Main_Routes/>
)
