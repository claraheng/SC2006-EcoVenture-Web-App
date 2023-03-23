import React from "react";
import ButtonBig from "./ButtonBig";

function HomePageMenuSection(){
    return(
        <div className="row">
        <div className="menu-item col-lg-6">
        <h1 className="menu-heading">I'm looking for a new adventure.</h1>
        <ButtonBig link="" label="Where Should I Go?"/>
        </div>
        
        <div className="menu-item col-lg-6">
        <h1 className="menu-heading">I'm already at my location!</h1>
        <ButtonBig link="" label="Check In"/>

        </div>
        </div>)
    }
    
export default HomePageMenuSection;