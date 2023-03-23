import React from "react";

function NavBar(){
    return(
       <nav className="navbar navbar-expand-lg navbar-dark">
            <a className="navbar-brand" href="">EcoVenture</a>
           
       <ul className="navbar-nav ms-auto"> 
            <li className="nav-item">
              <a className="nav-link" href="">My Account</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="">Log Out</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="">Log In</a>
            </li>
          </ul> 
          </nav>
    
        
    )
}

export default NavBar;