import React from "react";

function ButtonBig(props){
    return(
        <button type="button" class="btn btn-big" href={props.link}>{props.label}</button>
    )
}

export default ButtonBig;