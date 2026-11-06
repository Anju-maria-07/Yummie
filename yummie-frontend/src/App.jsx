import './App.css'
import { Navbar } from './components/NavBar';
import { Post } from './components/post';
import { Signup } from './pages/Signup';
import { Routes, Route } from 'react-router-dom';
import {Login} from './pages/login';
import {useState, useEffect} from 'react';
import {getCurrentUser} from './utils/auth';

function App() {

  const [user,setUser] = useState(null);

  useEffect(()=>{
    async function checkUser(){
      try{
        const userData = await getCurrentUser();
        setUser(userData);
      }
      catch(error){
        setUser(null);
      }
    }
    checkUser();
  },[])

  

  return (

    <Routes>
      <Route path='/' element={<> <Navbar />
      {user&& <p>Welcome, {user.username}</p>}
       <Post />
      
       </>} />
      <Route path='/signup' element={<Signup />} />
      <Route path='/login' element={<Login />} />
    </Routes>

  )
}

export default App
