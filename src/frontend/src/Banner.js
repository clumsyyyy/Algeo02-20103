import './Banner.css';
import DropBox from './components/DropBox';

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
            <br />
          </p> 
        </div>
        <DropBox />
       
    </div>
    
  );
}

export default Banner;
