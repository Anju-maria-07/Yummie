import './NavBar.css'

export  function Navbar() {
    return (

    <header className="header">
      <div><img src="images/logo.png" alt="Yummie logo" width="100px"></img></div>
      <div>
        <img src="images/search.png" width="50px" ></img>
        <input type="search" placeholder="Search" />
      </div>
    
      <nav className="nav">
        <a href="/" ><img src="images/Home.png" alt="Home" width="50px"  ></img></a>
        <a href="#"><img src="images/chat.png" alt="chat" width="50px"></img></a>
        <a href="#"><img src="images/Add.png" alt="Add post" width="50px"></img></a>
        <a href="#"><img src="images/notification.png" alt="notifications" width="50px"></img></a>
        <a href="#"><img src="images/profile.png" alt="profile" width="50px"></img></a>
      </nav>
    </header>
    )
}