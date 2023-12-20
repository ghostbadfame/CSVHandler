# CSVHandler

## Overview

This project is a web application that uses ReactJS for the front end, FastAPI for the backend, and MongoDB as the database. The main functionality of the application is to process CSV files uploaded by the user, store the data in a MongoDB database, and provide the CSV file values as output.

## Prerequisites

Before running the project, ensure that you have the following dependencies installed:

- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/)

## Installation

### Frontend (ReactJS)

1. Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Start the React development server:

    ```bash
    npm start
    ```

    The React app will be accessible at http://localhost:3000.

### Backend (FastAPI)

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

    The FastAPI server will be accessible at http://localhost:8000.

### Database (MongoDB)

Make sure you have MongoDB installed and running. Update the MongoDB connection settings in the `backend/main.py` file if needed.

## Usage

1. Open the web application in your browser: http://localhost:3000.

2. Upload a CSV file using the provided interface.

3. The backend will process the CSV file, store the data in the MongoDB database, and provide the CSV file values as output.

## Configuration

You can configure various settings in the `backend/main.py` file, including the MongoDB connection details and other application parameters.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.
