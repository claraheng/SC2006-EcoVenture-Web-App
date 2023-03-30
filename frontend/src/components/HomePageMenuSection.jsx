import React from "react";
import ButtonBig from "./ButtonBig";
import {useNavigate} from "react-router-dom";

function HomePageMenuSection(){
    const navigate=useNavigate();
    return(

        <div className="row">

        <div className="menu-item col-lg-6">
        <h1 className="menu-heading">I'm looking for a new adventure.</h1>
        <ButtonBig label="Where Should I Go?" onClick={(event)=>{navigate("/whereshouldigo",{replace:true})}}/>
        </div>
        
        <div className="menu-item col-lg-6">
        <h1 className="menu-heading">I'm already at my location!</h1>
        <ButtonBig label="Check In" onClick={(event)=>{navigate("/checkin",{replace:true})}}/>

        </div>
        
        </div>)
    }
    
export default HomePageMenuSection;