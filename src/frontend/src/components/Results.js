import React from 'react'
import "./Results.css"

export const Results = () =>{
    return(
        <div id = "Results" className = "Results" hidden>
            <link rel="stylesheet"
             href="//use.fontawesome.com/releases/v5.0.7/css/all.css">
                 </link>
            <h1>Bruh</h1>
            <div className = "containers">
                <div className = "container left">
                    Placeholder preview
                </div>

                <div className = "container right">
                    Placeholder results
                </div>

                <div className = "download">
                    <button class = "input-button right">
                        <i class = "fas fa-download"></i> Download
                    </button>
                </div>
            </div>
        </div>
    )
}

export default Results;