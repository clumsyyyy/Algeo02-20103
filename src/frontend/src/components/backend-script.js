import axios from 'axios'
import cors from 'cors'

const corsOptions = {
    origin: 'http://localhost:3000',
    credentials: true,
    optionSuccessStatus: 200
}
const uploadFile = () => {
    const data = new FormData()
    data.append('imageFile', this.state.selectedFile)
    console.log(data)
    axios.post("http://127.0.0.1:5000/v1/compress", data, {
    })
    .then(response => {
        console.log(response.statusCode)
    })
}

export default uploadFile;