export default function InputSearch({input_name="Search",image='src/assets/icons/search_icon.svg',input_placeholder}){
    const Set_focus = (element)=>{
        element.focus()
    }



    return (
        <div 
        className="border border-black rounded-2xl w-[500px] h-[40px] flex justify-between items-center" 
        onClick={()=>{Set_focus(document.getElementById("Search"))}}>

            <button className="mx-2 cursor-pointer">
                <img src={image} alt="" />
            </button>

            <input
            className="w-[90%] h-full rounded-2xl outline-none placeholder:font-light placeholder:text-black"
            type="search" 
            id="Search" 
            name={input_name} 
            placeholder={input_placeholder} autoComplete="True"/>

        </div>
    )
}