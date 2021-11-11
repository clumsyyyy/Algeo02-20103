import { FileDrop } from 'react-file-drop'
import './drag-drop.css'
import { useContext } from 'react'
import { ImgContext } from './ImageProvider.js'

export const DropBox = () => {
  const imgCtx = useContext(ImgContext);
  function SetImage(event){
    var files = event.target.files || event.dataTransfer;
    files = (files.files !== undefined ? files.files[0] : files[0]);
    if (!files) {
      alert("Tidak ada file!");
    } else {
      document.getElementById("Results").removeAttribute("hidden");
      document.getElementById("Results").scrollIntoView({ behavior: "smooth" });
      
      let reader = new FileReader();
      reader.onloadend = () => {
        imgCtx.setImage(files);
        document.getElementById("preview-box").src = reader.result;
      }
      reader.onerror = () => {
          alert("Tidak bisa membaca file!");
      }
      reader.readAsDataURL(files);
    }
  }

  return(
      <div className = "drag-drop">
          <label className = "input-button">
          <input type="file" accept = "image/*" onChange= {SetImage}></input>
          <i className = "fas fa-upload"></i> 
            Select Image </label> 
          <link rel="stylesheet"
            href="//use.fontawesome.com/releases/v5.0.7/css/all.css">
          </link>
          <FileDrop className = "drag-drop-box" onFrameDrop = {SetImage}>
          or drag your file here
          </FileDrop> 
    </div>
  )
}

export default DropBox