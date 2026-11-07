import {Outlet} from 'react-router-dom';
import {Navbar} from '../components/NavBar';

export function MainLayout(){
    return(
      <div>
        <Navbar />
        <Outlet />
      </div>
    );
}