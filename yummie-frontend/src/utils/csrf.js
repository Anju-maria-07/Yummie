
export async function getCsrfToken() {
    const response = await fetch('http://localhost:8000/api/users/csrf',
        {
            credentials : 'include'
        }
    );
    if (!response.ok){
        throw new Error('Failed to get csrf token');
    }
    const data = await response.json()
    return data.csrfToken;
}
