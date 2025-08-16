//imports
import { Link } from "react-router"

const FeaturedButton = ({button_content,link=null})=>{
    const html = (
        <button className="min-w-[100px] h-[40px] bg-featured cursor-pointer rounded-2xl text-white font-bold text-[16px]">
            {button_content}
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

export default FeaturedButton