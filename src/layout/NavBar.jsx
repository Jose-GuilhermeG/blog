//imports
import { Link } from "react-router";

//components
import InputSearch from "../components/inputs/InputSearch";
import IconButton from "../components/buttons/IconButton";
import FeaturedButton from "../components/buttons/FeaturedButton";


//navbar
const NavBar = ()=>(
    <nav className="w-full h-[10vh] flex items-center justify-between">
        <Link to='/'>
            Blog
        </Link>
        <InputSearch input_placeholder="Pesquisar Post ou Usuario"/>
        <ul className="flex justify-around items-center w-[20%]">
            <li>
                <IconButton icon='/src/assets/icons/write.svg' button_content='write'/>
            </li>
            <li>
                <FeaturedButton button_content="Sing up"/>
            </li>
        </ul>
    </nav>
)

export default NavBar