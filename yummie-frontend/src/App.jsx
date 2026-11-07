import './App.css'
import { Signup } from './pages/Signup';
import { Routes, Route, useNavigate } from 'react-router-dom';
import { Login } from './pages/login';
import { useState, useEffect } from 'react';
import { getCurrentUser, logoutUser } from './utils/auth';
import { MainLayout } from './layouts/MainLayout';
import { Home } from './pages/Home';
import {Chat} from './pages/Chat';

function App() {

  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    async function checkUser() {
      try {
        const userData = await getCurrentUser();
        setUser(userData);
      }
      catch (error) {
        setUser(null);
      }
    }
    checkUser();
  }, [])

  async function handleLogout() {
    try {
      await logoutUser();
      setUser(null);
      navigate('/login');
    }
    catch (error) {
      console.log('Logout error', error.message);
    }
  }

  return (

    <Routes>
      
      <Route path='/signup' element={<Signup />} />
      <Route path='/login' element={<Login />} />
      <Route element={<MainLayout />}>
        <Route path='/' element={<>
          {user && <p>Welcome, {user.username}</p>}
          <Home /> </>
        } />
        <Route path='/chat' element={<Chat />} />
      </Route>
    </Routes>

  )
}

export default App
