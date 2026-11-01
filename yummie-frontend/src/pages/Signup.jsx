import {useState} from 'react';
import './Signup.css'

export function Signup() {
    const [username,setUsername]=useState('');
    const [email,setEmail]=useState('');
    const [password,setPassword]=useState('');
    const [confirmPassword, setConfirmPassword]=useState('');
    return (
        <>
            <div className='signup-page'>
                <div className='signup-image'>

                    <div className='brand-message'>
                        <h1>Discover your people through every flavour</h1>
                        
                        <p className='brand-highlight'>
                            Good food. Great people. Real connections.

                        </p>
                        <div className='brand-divider'></div>
                        
                        <p className='brand-description'>
                            Connect over cravings, discover new flavors, 
                            and make food memories together.</p>
                    </div>

                </div>
                <div className="signup-form-container">
                    <img src='/images/logo.png'
                        alt='yummie logo'  />
                    <h2>Create your Account</h2>
                    <p>Join the Yummie community</p>
                    <form>
                        <div className='form-group'>
                            <label htmlFor='username'>Username</label>
                            <input type='text' id='username' name='username'
                                placeholder="Enter your username"
                                value={username}
                                onChange={(event)=>setUsername(event.target.value)} />
                        </div>

                        <div className='form-group'>
                            <label htmlFor="email">Email</label>
                            <input id='email' type='email' name='email'
                                placeholder='Enter your email'
                                value={email}
                                onChange={(event)=>setEmail(event.target.value)} 
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor='password'>Password</label>
                            <input type='password' id='password' name='password'
                                placeholder='Create a password'
                                value={password}
                                onChange={(event)=>setPassword(event.target.value)}
                            />
                        </div>

                        <div className='form-group'>
                            <label htmlFor='confirm-password'>Confirm Password</label>
                            <input type='password' id='confirm-password' name='confirmPassword'
                                placeholder='Enter your password again'
                                value={confirmPassword}
                                onChange={(event)=>setConfirmPassword(event.target.value)}
                            />
                        </div>

                        <button type='submit'>Create Account</button>
                    </form>

                    <p className='login-link'>
                        Already have an account?
                        <a href='/login'>Login</a>
                    </p>
                </div>

            </div>
        </>

    );
}