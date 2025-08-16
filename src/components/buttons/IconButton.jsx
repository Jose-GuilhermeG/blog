//imports
import { Link } from "react-router"

const IconButton = ({icon,button_content,link=null})=>{
    const html = (
        <button className="flex items-center justify-center cursor-pointer">
            <img src={icon} alt=""/>
            <span className="text-[20px] capitalize">
                {button_content}
            </span>
        </button>
    )

    if(link){
        return(
            <Link to={link}>
                {html}
            </Link>
        )
    }

    return html

}

export default IconButton