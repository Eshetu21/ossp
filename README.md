# Hate Speech Detector (using ML)

The Hate Speech Detector is an open source web app that identifies and classifies text as toxic or non-toxic. The application includes a preprocessing pipeline, a machine learning model, a FastAPI backend, and Next.js frontend.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Backend Setup (FastAPI)](#1-backend-setup-fastapi)
- [Frontend Setup (Next.js)](#2-frontend-setup-nextjs)
- [API Endpoints](#api-endpoints)
- [Dataset](#dataset)
- [License](#license)

## Features

- Preprocessing of raw datasets to clean and prepare the data.
- Machine learning pipeline using scikit-learn for text classification.
- REST API built with FastAPI to serve predictions.
- Frontend interface using Next.js.

## Prerequisites

Ensure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 16+](https://nodejs.org/)
- [npm](https://www.npmjs.com/)

## Setup

### 1. Backend Setup (FastAPI)

1. Clone the repository:
   ```bash
   git clone https://github.com/Eshetu21/ossp.git
   cd ossp/py
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Prepare the dataset:
   - Place the raw dataset file as `raw_dataset.csv` by creating a `data` folder.
   - Run the data preprocessing script:
     ```bash
     python preprocess_data.py
     ```
   - This will generate `cleaned_dataset.csv`.

5. Train the model:
   ```bash
   python train_model.py
   ```
   - This will generate the model file `hatespeech_model.pkl`.

6. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload --port 8000
   ```
   - The API will be available at `http://localhost:8000`.

### 2. Frontend Setup (Next.js)

1. Navigate to the frontend directory:
   ```bash
   cd ossp/next
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   - The application will be available at `http://localhost:3000`.

## API Endpoints

### `/predict` (POST)

- **Description:** Predicts whether a given comment is toxic or non-toxic.
- **Request Body:**
  ```json
  {
    "comment_text": "Your input comment here"
  }
  ```
- **Response:**
  ```json
  {
    "result": "non-toxic || toxic"
  }
  ```
## Dataset

The raw dataset used for this project is available for download:
- [Download Raw Dataset](https://drive.google.com/file/d/18nMJ6sbiyiI4T-MwmopysF4QoWzMU-Kp/view?usp=drive_link)
  
## Contribution
We welcome contributions from the community! Please read the [Contribution Guidelines](./CONTRIBUTING.md) for detailed instructions on how to contribute to this project.


## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
