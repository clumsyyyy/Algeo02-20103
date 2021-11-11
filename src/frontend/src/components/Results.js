import React, { useContext } from 'react'
import "./Results.css"
import axios from 'axios'
import { ImgContext } from './ImageProvider'

export const Results = () =>{
    const imgCtx = useContext(ImgContext);
    
    function ImageRes(){
        var height = document.getElementById("preview-box").naturalHeight;
        var width = document.getElementById("preview-box").naturalWidth;
        return Math.min(height, width * 3);
    }
    
    const uploadFile = () => {
        document.getElementById("results-div").removeAttribute("hidden");
        document.getElementById("results-div").scrollIntoView({ behavior: "smooth" });
        const data = new FormData()
        data.append('imageFile', imgCtx.image);
        var quality = document.getElementById('eigen-slider').value
        var eigenLimit = Math.round((parseInt(quality) / 100) * ImageRes())
        console.log(eigenLimit)
        data.append('eigenLimit', eigenLimit)
        axios.post("http://127.0.0.1:5000/v1/compress", data, {
            responseType: 'blob',
            headers : {
                'Content-Type' : 'multipart/form-data'
            },
        })
        .then(response => {
            let reader = new FileReader();
            reader.onloadend = (ev) => {
                imgCtx.setResultImg(ev.target.result);
            }
            reader.onerror = () => {
                alert("File tidak valid!");
            }
            reader.readAsDataURL(response.data);
            console.log(response.statusCode);
        })
    }

    const downloadFile = () => {
        const link = document.createElement('a');
        link.href = imgCtx.resultImg;
        link.setAttribute('download', imgCtx.image.name);
        link.click();
    }
    
    return(
        <div id = "Results" className = "Results" hidden>
            <link rel="stylesheet"href="//use.fontawesome.com/releases/v5.0.7/css/all.css"></link>
            <h1>Preview</h1>
            <div className = "containers">
                <img id = "preview-box" className = "container" alt = "preview"></img>
                    <div className = "slider-container">
                    <h3>Set Compression Rate</h3>
                    <p className = "left-p">Low</p>
                    <p className = "right-p">High</p>
                    <input id = "eigen-slider" type="range" min="1" max="100"></input>
                    
                </div>
                <div className = "download">
                    <button className = "input-button right" onClick = {uploadFile}>
                        Compress
                    </button>
                </div>
                <div id = "results-div" hidden>
                    <img id = "results-box" className = "container" alt = "results" src={imgCtx.resultImg}></img>
                    <div className = "download">
                        <button className = "input-button right" onClick={downloadFile}>
                            <i className = "fas fa-download"></i> Download
                        </button>
                    </div>
                </div>
            </div>
        </div>
    )
}
