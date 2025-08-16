//imports
import { Link } from "react-router";

//components
import InputSearch from "../components/inputs/InputSearch";


//navbar
const NavBar = ()=>(
    <nav>
        <Link to='/'>
            Blog
        </Link>
        <InputSearch/>
        <ul>
            
        </ul>
    </nav>
)

export default NavBar