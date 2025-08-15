import { BrowserRouter as Router,Routes,Route } from "react-router";

//pages
import App from "./pages/home";

const Main_Routes = ()=>(
    <Router>
        <Routes>
            <Route path="/" element={<App/>}/>
        </Routes>
    </Router>
)

export default Main_Routes