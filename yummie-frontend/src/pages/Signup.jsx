import './Signup.css'
export function Signup() {
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
                        alt='yummie logo' width="20px" />
                    <h2>Create your Account</h2>
                    <p>Join the Yummie community</p>
                    <form>
                        <div className='form-group'>
                            <label htmlfor='username'>Username</label>
                            <input type='text' id='username' name='username'
                                placeholder="Enter your username" />
                        </div>

                        <div className='form-group'>
                            <label htmlfor="email">Email</label>
                            <input id='email' type='email' name='email'
                                placeholder='Enter your email'
                            />
                        </div>
                        <div className="form-group">
                            <label htmlfor='password'>Password</label>
                            <input type='password' id='password' name='password'
                                placeholder='Create a password'
                            />
                        </div>

                        <div className='form-group'>
                            <label htmlfor='confirm-password'>Confirm Password</label>
                            <input type='password' id='password' name='password'
                                placeholder='Enter your password again'
                            />
                        </div>

                        <button type='submit'>Create Account</button>
                    </form>

                    <p classname='login-link'>
                        Already have an account?
                        <a href='/login'>Login</a>
                    </p>
                </div>

            </div>
        </>

    );
}