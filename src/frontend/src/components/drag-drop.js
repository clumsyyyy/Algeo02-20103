import React from 'react'
import { FileDrop } from 'react-file-drop'
import './drag-drop.css'


export const DropArea = () => {

    return(
        <div class = "drag-drop">
            <FileDrop
                onDrop = {() => alert("COCK")}
            >
            or drop your file here
            </FileDrop>
      </div>
    )
}

