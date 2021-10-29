import React from 'react'
import { FileDrop } from 'react-file-drop'
import './drag-drop.css'


export const DropArea = () => {
    const bruh = () => {
        alert("bruh");
        document.getElementById("Results").removeAttribute("hidden");
    document.getElementById("Results").scrollIntoView({ behavior: "smooth" });
    };

    return(
        <div class = "drag-drop">
            <link rel="stylesheet"
             href="//use.fontawesome.com/releases/v5.0.7/css/all.css">
            </link>
            <FileDrop
                onDrop = {() => alert("COCK")}
            >
                <label class = "input-button">
                <input type = "file" onClick = {bruh}></input>
                <i class = "fas fa-upload"></i> Upload Image
                </label>
            or drag your file here
            
            </FileDrop>
      </div>
    )
}

