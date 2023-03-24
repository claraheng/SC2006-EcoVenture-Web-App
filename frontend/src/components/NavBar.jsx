import React from "react";
import {useNavigate} from "react-router-dom"

function NavBar(){
  const navigate = useNavigate();
    return(
       <nav className="navbar navbar-expand-lg navbar-dark">
            <a className="navbar-brand" onClick={()=>{navigate("/homepage",{replace:true})}}>EcoVenture</a>
           
       <ul className="navbar-nav ms-auto"> 
            <li className="nav-item">
              <a className="nav-link" href="">My Account</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="">Log Out</a>
            </li>
          </ul> 
          </nav>
    
        
    )
}

export default NavBar;