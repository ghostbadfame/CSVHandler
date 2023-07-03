import { useEffect, useState } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';

function TableComponent() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/data');
      setData(response.data.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
 

  return (
    <div>
    <Button variant="contained" onClick={fetchData}>Get </Button>    
    <table>
      <thead>
        <tr>
          {/* <th>_id</th> */}
          <th>Date/Time</th>
          <th>Close</th>
          <th>High</th>
          <th>Low</th>
          <th>Open</th>
          <th>Volume</th>
          <th>Instrument</th>
        </tr>
      </thead>
      <tbody>
        {data.map((record, index) => (
          <tr key={index}>
            {/* <td>{record._id}</td> */}
            <td>{record.datetime}</td>
            <td>{record.close}</td>
            <td>{record.high}</td>
            <td>{record.low}</td>
            <td>{record.open}</td>
            <td>{record.volume}</td>
            <td>{record.instrument}</td>
          </tr>
        ))}
      </tbody>
    </table>
    </div>

    
  );
}

export default TableComponent;