import React from "react";
import SearchIcon from '@mui/icons-material/Search';

function SearchBar(props){
    return(
        <div className="search-bar">
            <SearchIcon className="search-icon"/><input className="search-input" placeholder={props.placeholder}/>
        </div>
        
    )
}

export default SearchBar;