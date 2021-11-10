import React from 'react'
import { FileDrop } from 'react-file-drop'
import './drag-drop.css'
import axios from 'axios'



export const DropArea = () => {    

    function ImageRes(){
        console.log(document.getElementById("preview-box").naturalHeight);
        console.log(document.getElementById("preview-box").naturalWidth);
    }
    const uploadFile = (imageFile) => {
        const data = new FormData()
        data.append('imageFile', imageFile)
        data.append('eigenLimit', 1)
        axios.post("http://127.0.0.1:5000/v1/compress", data, {
            headers : {
            'Content-Type' : 'multipart/form-data'
            },
        })
        .then(response => {
            console.log(response.statusCode)
        })
    }


    const buttonInput = (event) => {
        document.getElementById("Results").removeAttribute("hidden");
        document.getElementById("Results").scrollIntoView({ behavior: "smooth" });
        document.getElementById("preview-box").src = window.URL.createObjectURL(event.target.files[0])
        uploadFile(event.target.files[0])
        setTimeout(ImageRes, 500)
    };

    const onFileInputChange = (event) => {
        var files = event.target.files || event.dataTransfer
        if (files){
            document.getElementById("Results").removeAttribute("hidden");
            document.getElementById("Results").scrollIntoView({ behavior: "smooth" });
            document.getElementById("preview-box").src = window.URL.createObjectURL(files.files[0])
        }
        else{
            alert("Tidak ada file!")
        } 
    }

    return(
        <div className = "drag-drop">
            <link rel="stylesheet"
             href="//use.fontawesome.com/releases/v5.0.7/css/all.css">
            </link>
            <FileDrop onFrameDrop = {onFileInputChange}>
                <label className = "input-button">
                <input type="file" accept = "image/*" onChange= {buttonInput}></input>
                <i className = "fas fa-upload"></i> 
                Upload Image </label> 
                or drag your file here
        
            </FileDrop>
            
      </div>
    )
}

