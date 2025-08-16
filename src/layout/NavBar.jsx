//imports
import { Link } from "react-router";

//components
import InputSearch from "../components/inputs/InputSearch";
import IconButton from "../components/buttons/IconButton";


//navbar
const NavBar = ()=>(
    <nav className="w-full h-[10vh] flex items-center justify-between">
        <Link to='/'>
            Blog
        </Link>
        <InputSearch input_placeholder="Pesquisar Post ou Usuario"/>
        <ul>
            <li>
                <IconButton icon='/src/assets/icons/write.svg' button_content='write' link='' />
            </li>
            <li>

            </li>
        </ul>
    </nav>
)

export default NavBar