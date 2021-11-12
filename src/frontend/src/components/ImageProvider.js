import React, { createContext, useState } from "react";

export const ImgContext = createContext({
    image: null,
    setImage: null,
    resultImg: null,
    setResultImg: null,
    compressionTime: null,
    setCompressionTime: null,
    compressionRate: null,
    setCompressionRate: null
});

export function ImgProvider({ children }){
    const [image, setImage] = useState(null);
    const [resultImg, setResultImg] = useState(null);
    const [compressionTime, setCompressionTime] = useState(null);
    const [compressionRate, setCompressionRate] = useState(null);
    return(
        <ImgContext.Provider
            value = {{ image, setImage, resultImg, setResultImg, compressionTime, setCompressionTime, compressionRate, setCompressionRate }}
        > 
            {children}
        </ImgContext.Provider>
    );
}
