import { useState } from 'react';
import { loginUser } from '../utils/auth'
import { useNavigate, Link, useLocation } from 'react-router-dom';
import './Signup.css';


export function Login() {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    

    const navigate = useNavigate();
    const location = useLocation();

    async function handleSubmit(event) {
        event.preventDefault();
        setError('');
        

        if (!username.trim() || !password) {
            setError('please fill all fields !')
            return;
        }
        try {
            await loginUser(username, password);

            navigate('/')
        }
        catch (error) {
            setError(error.message || 'Login failed. Please try again !.')
        }
    }

    return (
        <div className='signup-page'>
            <div className='signup-image'>
                <div className='brand-message'>
                    <h1>Welcome back to yummie!</h1>

                    <p className='brand-highlight'>
                        Good Food.Great People.Real Connections</p>
                    <div className='brand-divider'></div>
                    <p className='brand-description'>
                        Time to discover your next favorite ! </p>
                </div>
            </div>

            <div className='signup-form-container'>
                <img src='/images/logo.png' alt='yummie logo' />
                {location.state?.message && 
                <p className='success-message'>{location.state.message}</p>}

                <h2>Login to your account</h2>
                <p>Join the Yummie community</p>
                <form onSubmit={handleSubmit}>
                    <div className='form-group'>
                        <label htmlFor='username'>Username</label>
                        <input type='text' id='username' name='username' placeholder='Enter your username'
                            value={username}
                            onChange={(event) => setUsername(event.target.value)} />

                    </div>
                    <div className='form-group'>
                        <label htmlFor='password'>Password</label>
                        <input type='password' id='password' placeholder='Enter your password' name='password'
                            value={password}
                            onChange={(event) => setPassword(event.target.value)} />
                    </div>
                    <button type='submit'>Login</button>
                </form>
                {error && <p className='error-message'>{error}</p>}
                
                <p>Don't have an account?{'  '}
                  <Link to='/signup' >sign up</Link>
                </p>
                   
            </div>
        </div>
    )

}