import React, { useContext } from 'react'
import "./Results.css"
import axios from 'axios'
import { ImgContext } from './ImageProvider'

export const Results = () =>{
    const imgCtx = useContext(ImgContext);
    
    const uploadFile = () => { 
        var scale = parseInt(document.getElementById('scale').value);
        var iteration = parseInt(document.getElementById('iter').value);
        if (scale <= 0 || scale > 100 || isNaN(scale)){
            alert("Nilai skala harus di antara 1 hingga 100!")
        } else if (iteration <= 0 || iteration > 100 || isNaN(iteration)){
            alert("Nilai iterasi harus di antara 1 hingga 100!")
        } else {
            imgCtx.setIsProcessing(true);
            imgCtx.setResultImg(null);
            imgCtx.setCompressionRate(null);
            imgCtx.setCompressionTime(null);
            
            var eigenRatio = parseInt(document.getElementById('eigen-slider').value) / 100;
            var alphaBool = document.getElementById('alpha-checkbox').value === "on" ? true : false

            const data = new FormData()
            data.append('imageFile', imgCtx.image);
            data.append('eigenRatio', eigenRatio);
            data.append('scale', scale);
            data.append('preserveAlpha', alphaBool);
            data.append('iteration', iteration);

            document.getElementById("image-waiting").removeAttribute("hidden");
            document.getElementById("image-waiting").scrollIntoView({ behavior: "smooth" });
            document.getElementById("results-div").setAttribute("hidden", 'true');

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
                    imgCtx.setIsProcessing(false);
                }
                reader.onerror = () => {
                    alert("File tidak valid!");
                }
                reader.readAsDataURL(response.data);
                imgCtx.setCompressionTime(response.headers['x-compression-time'])
                imgCtx.setCompressionRate(response.headers['x-compression-rate'])
                document.getElementById("results-div").removeAttribute("hidden");
                document.getElementById("results-div").scrollIntoView({ behavior: "smooth" });
                document.getElementById("image-waiting").setAttribute("hidden", 'true');
            })
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
                    <h3 className = "section-title">Set Eigen Ratio</h3>
                    <p className = "left-p">Low</p>
                    <p className = "right-p">High</p>
                    <input id = "eigen-slider" type="range" min="1" max="100"></input>
                    <p className = "expository-paragraph"><br/>Higher Eigen Ratio means a sharper compressed image quality albeit more time to process.</p>
                </div>

                <div className = "scale-input">
                    <h3 className = "section-title"> Set Image Scale </h3>
                    <input className = "scale" id = "scale" type = "number" placeholder = "Enter image scale... (1-100)" required min = "1" max = "100"></input>
                    <p className = "expository-paragraph">Higher image scale will create a higher-resolution compressed image albeit more time to process.</p>
                </div>

                <div className = "iter-input">
                    <h3 className = "section-title"> Set Iteration</h3>
                    <input className = "iter" id = "iter" type = "number" placeholder = "Enter iteration number... (1-100)" required min = "1" max = "100"></input>
                    <p className = "expository-paragraph">Higher iteration count would take more time, but may result in better image quality.</p>
                </div>

                <div className = "alpha-layer">
                    <label htmlFor = "alpha-checkbox">
                        Preserve alpha layer? &nbsp;&nbsp;&nbsp;
                        <input id = "alpha-checkbox" type = "checkbox"></input>
                    </label>
                    <p className = "expository-paragraph">(mark for images with transparent elements)</p>
                </div>

                <div className = "download">
                    <button className = "input-button right" onClick= {uploadFile}>Compress!
                    </button>
                </div>
                        
                <div id = "image-waiting" hidden>
                    <p className = "loading-text"> Processing the image. <br/>
                    This may take a while </p>
                </div>

                <div id = "results-div" hidden>
                    <img id = "results-box" className = "container" alt = '' src={imgCtx.resultImg}></img>
                    <p className = "expository-paragraph">Compression time: {parseFloat(imgCtx.compressionTime).toFixed(3)}s</p>
                    <p className = "expository-paragraph">Compression rate: {parseFloat(imgCtx.compressionRate).toFixed(4) * 100}%</p>
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
