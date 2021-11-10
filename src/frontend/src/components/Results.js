import React from 'react'
import "./Results.css"
import axios from 'axios'
import Slider from '@mui/material/Slider'
export const Results = () =>{

    function ImageRes(){
        var height = document.getElementById("preview-box").naturalHeight;
        var width = document.getElementById("preview-box").naturalWidth;
        return Math.min(height, width * 3)
    }

    

    const downloadFile = () =>{
        axios.post('http://127.0.0.1:5000/v1/compress', {
            responseType: 'blob',
            Headers: {
                'Content-Type' : 'multipart/form-data'
            },
        }).then((response) => {
            const url = window.URL.createObjectURL(new Blob([response.data]))
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'compressed.jpg')
            document.body.appendChild(link);
            link.click();
        })
    }
        
    return(
        <div id = "Results" className = "Results" hidden>
            <link rel="stylesheet"href="//use.fontawesome.com/releases/v5.0.7/css/all.css"></link>

            <h1>Preview</h1>

            <div className = "containers">

                <img id = "preview-box" className = "container" alt = "preview"></img>
                <div className = "slider-container">
                    <p>Eigen limit (in percentage)</p>
                    <Slider defaultValue={50} aria-label="Default" valueLabelDisplay="auto"/>
                </div>
                
                <div className = "download">
                    <button className = "input-button right">
                        Compress
                    </button>
                </div>

                <img id = "results-box" className = "container" alt = "results"></img>
                <div className = "download">
                    <button className = "input-button right" onClick = {downloadFile}>
                        <i className = "fas fa-download"></i> Download
                    </button>
                </div>
            </div>
        </div>
    )
}
