import React from "react";
import MenuSection from "./MenuSection";
import NavBar from "./NavBar";
import TitleSection from "./TitleSection";


function HomePage(){
    return(
        <section>
        <div className="colored-section container-fluid">
        <NavBar/>
        <TitleSection/>
        
        </div>
        
        <div>
        <MenuSection/>
        </div>
        </section>
        )
    }
    
    export default HomePage;