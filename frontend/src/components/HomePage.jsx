import React from "react";
import MenuSection from "./HomePageMenuSection";
import NavBar from "./NavBar";
import TitleSection from "./TitleSection";


function HomePage(){
    return(
        <section>
        <div className="colored-section container-fluid">
        <NavBar/>
        <TitleSection title="Welcome to EcoVenture." description="Embark on your next adventure at one of our Fitness Areas."/>
        
        </div>
        
        <div>
        <MenuSection/>
        </div>
        </section>
        )
    }
    
    export default HomePage;