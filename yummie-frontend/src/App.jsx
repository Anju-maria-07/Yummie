import './App.css'
import { Navbar } from './components/NavBar'
import { Post } from './components/post'
import { Signup } from './pages/Signup'
import { Routes, Route } from 'react-router-dom'

function App() {

  return (

    <Routes>
      <Route path='/' element={<> <Navbar /> <Post /> </>} />
      <Route path='/signup' element={<Signup />} />
    </Routes>

  )
}

export default App
