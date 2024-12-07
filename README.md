# Credit Card Fraud Detection API

## Project Structure
- `app.py`: Contains the Flask application setup and API routes.
- `random_forest_model.pkl`: The serialized RandomForest model ready for prediction.
- `requirements.txt`: Lists all Python libraries that need to be installed.
- `README.md`: Documentation for setting up, running, and using the application.

## Project Description
This project implements a machine learning model to detect fraudulent transactions using a RandomForest classifier trained on highly anonymized data, primarily derived from PCA transformations. The objective is to provide a scalable and effective solution for identifying potentially fraudulent activities in transaction data. The model is deployed through a Flask-based REST API, which serves as an interface to receive transaction data and return predictions.

## Features
- **RandomForest Model**: Utilizes RandomForestClassifier for robust fraud detection.
- **Flask API**: A REST API to provide real-time predictions on transaction data.
- **Security Measures**: Implements basic security features for safe API interactions.

## Requirements
To run this project, you will need Python 3.8 or newer.

## Installation Instructions

### Clone the repository
```bash
git clone https://github.com/biplove-georgian/AIDI1003_FinalProject.git
cd AIDI1003_FinalProject
```

### Install Dependencies
```pip install -r requirements.txt```

### Usuage Guide

#### Running the Flask API
```python app.py```

This command initializes a local server, typically hosted at ```http://127.0.0.1:5001/```.

#### Prediction
To make predictions, send a POST request to the API with transaction data. This can be done using tools like Postman or through a CURL command:
```http://127.0.0.1:5001/predict```

In Postman:
You can post the above url using post method passing the following raw json in body:
```[
    {
        "Time": 10000,
        "V1": -0.1,
        "V2": 0.5,
        "V3": 0.1,
        "V4": -0.1,
        "V5": -0.2,
        "V6": 0.1,
        "V7": 0.1,
        "V8": -0.1,
        "V9": 0.0,
        "V10": -0.1,
        "V11": 0.1,
        "V12": 0.1,
        "V13": 0.0,
        "V14": 0.1,
        "V15": -0.1,
        "V16": 0.1,
        "V17": 0.0,
        "V18": -0.1,
        "V19": 0.0,
        "V20": 0.2,
        "V21": 0.0,
        "V22": 0.1,
        "V23": -0.1,
        "V24": 0.0,
        "V25": 0.1,
        "V26": -0.1,
        "V27": 0.0,
        "V28": 0.1,
        "Amount": 50.0
    },
    {
        "Time": 80000,
        "V1": -4,
        "V2": 5,
        "V3": -7,
        "V4": 8,
        "V5": -3,
        "V6": -2,
        "V7": -5.5,
        "V8": 3,
        "V9": -2,
        "V10": -5,
        "V11": 3.5,
        "V12": -6,
        "V13": 0.5,
        "V14": -7,
        "V15": 0.8,
        "V16": -4,
        "V17": 6,
        "V18": -3,
        "V19": 2,
        "V20": 1.2,
        "V21": 0.9,
        "V22": -0.5,
        "V23": 0.4,
        "V24": -1.5,
        "V25": 2.2,
        "V26": 0.7,
        "V27": -0.3,
        "V28": 0.4,
        "Amount": 1200.0
    }
]
```

## Results
You will see the results based on the inputs passed as whether each transaction is classified as fraud or not.



