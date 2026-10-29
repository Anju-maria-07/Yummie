import {useState} from 'react';
import {Heart} from 'lucide-react';
import './post.css';

export function Post() {
    const [liked,setLiked]=useState(false);

    const heartIcon=<Heart 
        size={20}
        fill={liked? 'chocolate':'none'}
        color={liked? 'chocolate':'currentColor'}
    />
    const likeText=liked? 'Liked':'Like'

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
                    <button onClick={()=>{
                     setLiked(previousLiked => !previousLiked);   
                    }}
                    >
                        {heartIcon}
                        {likeText}
                        </button>
                    <button>comment</button>

                </div>
                <p className='caption'>Hydrabadi chicken biriyani!</p>
                <p className='hashtags'> #biriyani #foodies </p>
            </div>
        </article>
    );
}