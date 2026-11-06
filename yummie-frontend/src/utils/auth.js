import {getCsrfToken} from './csrf'

export async function loginUser(username, password){
    const csrfToken = await getCsrfToken();

    const response =await fetch('http://localhost:8000/api/users/login/',
        {
            method:'POST',
            credentials:'include',
            headers:{
                'content-type':'application/json',
                'X-CSRFToken': csrfToken,
            },
            body:JSON.stringify({
                username:username,
                password:password
            })
        }
    );
    const data = await response.json();
    
    if (!response.ok){
        throw new Error(data.error || 'Login failed. Please try again !')
    }
    return data;
}

export async function getCurrentUser(){
    const response= await fetch('http://localhost:8000/api/users/me/',
        {
            credentials:'include'
        }
    )
    if(!response.ok){
        throw new Error('not Authenticated')
        
    }
    return await response.json()

}

export async function logoutUser(){
    const csrfToken = await getCsrfToken();

    const response = await fetch(
        'http://localhost:8000/api/users/logout/',
        {
            method:'POST',
            credentials :'include',
            headers:{
                'X-CSRFToken': csrfToken,
            },
        }
    )
    const data = await response.json();

    if(!response.ok){
        throw new Error(data.error ||'Failed to logout');
    }
    return data
}