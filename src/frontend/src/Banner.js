import './Banner.css';
import { DropArea } from './components/drag-drop.js';

function Banner() {
  return (
    <div className="banner">
        <div className = "title">
          Totally a Normal Title 
          <br/>
          for an Image Compression Web
        </div>
        <div className = "info-box">
          <p className = "info">
            This is an image compression service using Singular Value Decomposition
            <br />Bepis Epic goes Brrrr
          </p> 
        </div>
        <DropArea/>
        <p className = "info">made by amer benis and newo</p>
    </div>
    
  );
}

export default Banner;
