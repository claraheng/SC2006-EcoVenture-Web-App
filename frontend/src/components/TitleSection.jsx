import React from "react"

function TitleSection(props){
    return(
        <div className="title-section">
            <h1 className="title">{props.title}</h1>
            <h3 className="description">{props.description}</h3>
        </div>
    )
}

export default TitleSection;