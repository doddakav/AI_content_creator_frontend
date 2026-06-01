# AI Content Creator Frontend

## Overview

This is the frontend application for the AI Content Creator project. The frontend is built using Streamlit and provides a user-friendly interface for generating AI-powered content.

Users can:

* Enter a topic
* Select a technology
* Choose a content type
* Select a writing tone
* Generate content using AI

The frontend communicates with the FastAPI backend through REST APIs.

---

## Features

* Interactive UI using Streamlit
* Topic-based content generation
* Multiple content formats
* Multiple tone options
* Real-time content generation
* Backend API integration

---

## Technologies Used

* Python
* Streamlit
* Requests

---

## Project Structure

frontend/

├── app.py

├── .streamlit/

│   └── secrets.toml

└── requirements.txt

---

## Installation

### Clone Repository

git clone <repository-url>

cd frontend

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

---

## Configuration

Create:

.streamlit/secrets.toml

Add:

api_url="http://127.0.0.1:8000"

For deployed backend:

api_url="https://your-backend-url.onrender.com"

---

## Run Application

streamlit run app.py

Default URL:

http://localhost:8501

---

## User Workflow

1. Enter topic.
2. Select technology.
3. Select content type.
4. Select tone.
5. Click Generate Content.
6. View AI-generated content.

---

## Future Enhancements

* Copy content button
* Download as PDF
* Dark mode support
* Content history
* Word count display
* Export to DOCX

---

## Dependencies

streamlit

requests
