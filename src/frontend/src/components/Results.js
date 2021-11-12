import React, { useContext } from 'react'
import "./Results.css"
import axios from 'axios'
import { ImgContext } from './ImageProvider'

export const Results = () =>{
    const imgCtx = useContext(ImgContext);
    
    const uploadFile = () => { 
        imgCtx.setResultImg(null);
        imgCtx.setCompressionRate(null);
        imgCtx.setCompressionTime(null);
        document.getElementById("results-div").removeAttribute("hidden");
        document.getElementById("results-div").scrollIntoView({ behavior: "smooth" });
        const data = new FormData()
        data.append('imageFile', imgCtx.image);
        var quality = document.getElementById('eigen-slider').value;
        var eigenRatio = parseInt(quality) / 100;
        data.append('eigenRatio', eigenRatio);
        var scale = parseInt(document.getElementById('scale').value);
        console.log(scale)
        if (1 <= scale <= 100 && !isNaN(scale)){
            data.append('scale', scale);
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
                imgCtx.setCompressionTime(response.headers['x-compression-time'])
                imgCtx.setCompressionRate(response.headers['x-compression-rate'])
            })
        } else {
            alert("Scale value must be from 1 to 100!")
        }
        
        
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
            <div className = "containers">
                <img id = "preview-box" className = "container" alt = "preview"></img>
                    <div className = "slider-container">
                    <h3>Set Eigen Ratio</h3>
                    <p className = "left-p">Low</p>
                    <p className = "right-p">High</p>
                    <input id = "eigen-slider" type="range" min="1" max="100"></input>
                    <p className = "expository-paragraph"><br/>Lower Eigen Ratio means lower image quality, while higher Eigen Ratio
                    means higher image quality. Higher Eigen Ratio may take more time to process.</p>
                </div>

                <div className = "scale-input">
                    <h3> Set Image Scale</h3>
                    <input className = "scale" id = "scale" type = "number" placeholder = "Enter image scale..." required min = "1" max = "100"></input>
                    <p className = "expository-paragraph">Input the scale number from 1 to 100. A lower scale will result in an image with a lower resolution,
                    while a higher image scale will result in a sharper image albeit more time to process.</p>
                </div>
                <div className = "download">
                    <button className = "input-button right" onClick= {uploadFile}>Compress!
                    </button>
                </div>
                <div id = "results-div" hidden>
                    <p> Processing the image. <br/>
                    This may take a while.... </p>
                    <img id = "results-box" className = "container" alt = '' src={imgCtx.resultImg}></img>
                    <p className = "expository-paragraph">Compression time: {parseFloat(imgCtx.compressionTime).toFixed(5)}</p>
                    <p className = "expository-paragraph">Compression rate: {parseFloat(imgCtx.compressionRate).toFixed(5)}</p>
                    <div className = "download">
                        <button className = "input-button download-button" onClick={downloadFile}>
                            <i className = "fas fa-download"></i> &nbsp; Download
                        </button>
                    </div>
            
                </div>
                <div className = "footer">
                    2021, 'Newo Social Credit'
                </div>
            </div>
        </div>
    )
}
