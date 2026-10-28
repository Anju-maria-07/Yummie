import './post.css'

export function Post() {
    return (
        <article className='food-post'>
            <div className="post-header">
                <div className="user-info" >
                    <img src="images/profile-pic1.jpg" ></img>
                    <span>Maria Jacob</span>
                </div>
            </div>

            <img src="images/food-post/chicken-hyderabadi-biryani-01.jpg" ></img>

            <div> post-content
                <div>post actions
                    <button>Like</button>
                    <button>comment</button>

                </div>
                <p>caption</p>
                <p> #hashtags</p>
            </div>
        </article>
    );
}