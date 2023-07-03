import './App.css';
import Button from '@mui/material/Button';
import { useState } from 'react';
import axios from 'axios';
// import fetchdata from './TableComponent'

function App() {
  const [file, setFile] = useState(null);

  const handleChange = (event) => {
    setFile(event.target.files[0])
  }

  const upload = async() => {
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const response = await axios.post('http://localhost:8000/upload', formData);
      console.log(response.data); 
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  }
  return (
    <div className="App">
       <input type='file' onChange={handleChange} />
            <Button variant="contained" onClick={upload}>Upload </Button>
        

    </div>
  );
}

export default App;
