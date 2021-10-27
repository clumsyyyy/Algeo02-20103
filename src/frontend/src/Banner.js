import './Banner.css';
import { DropArea } from './components/drag-drop.js';

function Banner() {
  return (
    <div className="banner">
        <div className = "title">
          Benis Compressor Mk1
        </div>
        <div className = "info-box">
          <p>Please upload your image.</p>
        </div>
        <label class = "input-button">
          <input type = "file"></input>
          <i>Input your image...</i>
        </label>

        <DropArea/>
    </div>
  );
}

export default Banner;
