import React from "react";

/**
 * 
 * @param {*} onClick function to call when clicked
 * @param {*} label label on button
 * @returns 
 */
function ButtonBig(props){
    return(
   <button type="button" onClick={props.onClick} class="btn btn-big">{props.label}</button>
    )
}

export default ButtonBig;