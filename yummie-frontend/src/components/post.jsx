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

            <img src="images/food-post/chicken-hyderabadi-biryani-01.jpg" 
            alt='hydrabadi chicken biriyani'
            className="food-image" ></img>

            <div className="post-content"> 
                <div className="post-actions" >
                    <button>Like</button>
                    <button>comment</button>

                </div>
                <p className='caption'>Hydrabadi chicken biriyani!</p>
                <p classname='hashtags'> #biriyani #foodies </p>
            </div>
        </article>
    );
}