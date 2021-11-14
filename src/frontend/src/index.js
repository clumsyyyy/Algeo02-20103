import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Banner from './Banner';
import { Results } from './components/Results.js'
import reportWebVitals from './reportWebVitals'
import { ImgProvider } from './components/ImageProvider.js'


ReactDOM.render(
  <React.StrictMode>
    <ImgProvider>
      <Banner />
      <Results />
    </ImgProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
