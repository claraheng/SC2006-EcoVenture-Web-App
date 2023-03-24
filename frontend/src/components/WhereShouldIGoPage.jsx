import React from "react";
import NavBar from "./NavBar";
import SearchBar from "./SearchBar";
import TitleSection from "./TitleSection";
import MenuSection from "./WSIGPageMenuSection";

function WhereShouldIGo(){
    return(
        <div>
        <div className="colored-section container-fluid">
            
                
            <NavBar/>
            <TitleSection title="Where Should I Go?" description="Choose a location category."/>
        </div>
        <SearchBar placeholder="Search for Fitness Areas..."/>

            <MenuSection/>
                
            
        </div>
    )
}

export default WhereShouldIGo;