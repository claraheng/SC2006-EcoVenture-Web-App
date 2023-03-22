import React from "react";

function MenuSection(){
    return(
        <div className="row">
        <div className="menu-item col-lg-6">
        <h1 className="menu-heading">I'm looking for a new adventure.</h1>
        <button type="button" class="btn btn-big">Where Should I Go?</button>
        </div>
        
        <div className="menu-item col-lg-6">
        <h1 className="menu-heading">I'm already at my location!</h1>
        <button type="button" class="btn btn-big">Check In</button>
        </div>
        </div>)
    }
    
export default MenuSection;