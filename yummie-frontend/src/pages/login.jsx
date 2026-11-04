
export function Login(){
    return(
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
                <h2>Login to your account</h2>
                <p>Join the Yummie community</p>
                <form>
                    <div className='form-group'>
                        <label htmlFor='username'>Username</label>
                        <input id='username' name='username' placeholder='Enter your username' />

                    </div>
                    <div className='form-group'>
                        <label htmlFor='password'>Password</label>
                        <input id='password' placeholder='Enter your password' name='password' />
                    </div>
                    <button>Login</button>
                </form>
                <p>Don't have an account? 
                    <a href='/signup'>Sign up</a></p>
            </div>
        </div>
    )

}