from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import csv
from pydantic import BaseModel
from pymongo import MongoClient
import json

app = FastAPI()

origins = [
    "http://localhost"
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,

    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with the URL of your frontend
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

client = MongoClient( 'mongodb+srv://mongo_id:password@cluster0.8oexlkc.mongodb.net/?retryWrites=true&w=majority')
db = client['Cluster0']
collection = db['test']

class Item(BaseModel):
    datetime: str
    close: str
    high: str
    low: str
    open: str
    volume: str
    instrument: str

# @app.get("/test")
# async def test():
#     return {"message": "Test endpoint"}
# @app.get("/data")
# async def get_data():
#     data = []
#     for record in collection.find():
#         data.append(record)
#     return {"data":data} 


@app.get("/data")
async def get_data():
    data = []
    for record in collection.find():
        record["_id"] = str(record["_id"])  # Convert ObjectId to string
        data.append(record)
    return {"data": data}
      
  
    

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()  # Read the contents of the uploaded file

    # Convert CSV to JSON
    csv_data = contents.decode('utf-8').splitlines()
    reader = csv.DictReader(csv_data)
    json_data = json.dumps(list(reader))
    
    
    # Remove the unnecessary backslashes from the string
    cleaned_data = json_data.replace("\\", "")

    # Remove the extra quotes around the entire string
    cleaned_data = cleaned_data[1:-1]

    # Replace the individual strings with commas
    cleaned_data = cleaned_data.replace('", "', '", "')

    # Add square brackets to make it a valid JSON array
    cleaned_data = f"[{cleaned_data}]"

    # Load the cleaned data as JSON
    parsed_data = json.loads(cleaned_data)

    # Print the formatted JSON
    formatted_data = json.dumps(parsed_data, indent=2)

    cleaned_data = formatted_data.replace("\n", "").replace("  ", "")

    # Convert cleaned data to Python objects
    records = json.loads(cleaned_data)

    # Insert records into MongoDB
    collection.insert_many(records)

    # for row in cleaned_data:
    #     item_data = {
    #         "datetime": row['datetime'],
    #         "close": float(row['close']),
    #         "high": float(row['high']),
    #         "low": float(row['low']),
    #         "open": float(row['open']),
    #         "volume": int(row['volume']),
    #         "instrument": row['instrument'],
    #     }
    #     collection.insert_one(item_data)

    # return {"message": "Data uploaded successfully"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# async def upload_csv(item: Item, file: UploadFile = File(...)):
#     contents = await file.read() 
#     # return{'filename':len(contents)}
#     csv_data = contents.decode('utf-8').splitlines()
#     reader = csv.DictReader(csv_data)
#     print(reader)

#     for row in json_data:
#         item_data = {
#             "datetime": row['datetime'],
#             "close": float(row['close']),
#             "high": float(row['high']),
#             "low": float(row['low']),
#             "open": float(row['open']),
#             "volume": int(row['volume']),
#             "instrument": row['instrument'],
#         }
#         collection.insert_one(item_data)

#     return {"message": "Data uploaded successfully"}
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

