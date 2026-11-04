import './App.css'
import { Navbar } from './components/NavBar'
import { Post } from './components/post'
import { Signup } from './pages/Signup'
import { Routes, Route } from 'react-router-dom'
import { getCsrfToken } from './utils/csrf'
import {Login} from './pages/login'

function App() {

  async function testCsrf() {
    try{
      const token = await getCsrfToken();
      console.log('Csrf token received: ', token);
    }
    catch(error){
      console.log('scrf error: ',error);
    }
  }

  return (

    <Routes>
      <Route path='/' element={<> <Navbar /> <Post />
      <button onClick={testCsrf}>TestCsrf</button>
       </>} />
      <Route path='/signup' element={<Signup />} />
      <Route path='/login' element={<Login />} />
    </Routes>

  )
}

export default App
