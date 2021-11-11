import React, { createContext, useState } from "react";

export const ImgContext = createContext({
    image: null,
    setImage: null,
    resultImg: null,
    setResultImg: null
});

export function ImgProvider({ children }){
    const [image, setImage] = useState(null);
    const [resultImg, setResultImg] = useState(null);

    return(
        <ImgContext.Provider
            value = {{ image, setImage, resultImg, setResultImg }}
        > 
            {children}
        </ImgContext.Provider>
    );
}
