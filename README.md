# Text-to-Speech API with ElevenLabs & FastAPI
 
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/) 

---

## Overview

**Text-to-Speech ElevenLabs FastAPI** is a modern, lightweight API built with **FastAPI** that converts text into natural-sounding speech using **ElevenLabs TTS**. It allows developers to quickly integrate realistic voice generation into their applications with minimal setup.  

The project also includes a simple front-end interface for testing text-to-speech functionality directly in the browser.

## Features

- Convert text to speech using ElevenLabs API  
- FastAPI-based RESTful endpoints for easy integration  
- Async support for efficient performance  
- Dockerized for seamless deployment  
- Easily extendable architecture with modular services, routers, and schemas  

## Demo

You can test the API locally or integrate it with your applications. Example endpoint:
<img width="1919" height="908" alt="image" src="https://github.com/user-attachments/assets/e26ec8e5-0c10-414a-ba41-f071d30bab0a" />
<img width="1199" height="928" alt="image" src="https://github.com/user-attachments/assets/ed414f31-6aa6-4364-ad75-abe7d41f6755" />


```http
POST /tts
Content-Type: application/json

{
  "text": "Hello, this is a test."
}


```
## Project Structure
```bash
tts-fastapi/
├── app/
│ ├── core/ # Configuration and application settings
│ ├── routers/ # API endpoints
│ ├── schemas/ # Request and response models
│ └── services/ # Business logic and ElevenLabs API integration
├── tests/ # Unit tests
├── Dockerfile # Docker container setup
├── requirements.txt # Python dependencies
├── index.html # Frontend interface for testing TTS
└── .env # Environment variables (API keys)
```


---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/riponalmamun/Text-to-Speech-ElevenLabs-FastAPI.git
cd Text-to-Speech-ElevenLabs-FastAPI
```
2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt


```

Configure environment variables:

3. Create a .env file in the root directory with your ElevenLabs API key:
```bash
ELEVENLABS_API_KEY=your_api_key_here

```
4. Run the FastAPI server:

```bash
uvicorn app.main:app --reload

```
Access the API at: http://127.0.0.1:8000
API documentation available at: http://127.0.0.1:8000/docs

## Usage Example

POST Request to /tts endpoint:
```bash
POST /tts
Content-Type: application/json

{
  "text": "Hello, this is a test using ElevenLabs TTS."
}

```
Response: MP3 audio file containing the generated speech.

## Running Tests

Run unit tests using pytest:
```bash
pytest

```

## Docker Deployment

Build and run the project using Docker:
```bash
docker build -t tts-fastapi .
docker run -p 8000:8000 tts-fastapi

```

## VContributing

Contributions are welcome! Please open issues or submit pull requests to improve features, fix bugs, or enhance documentation.
```bash

```
License

This project is licensed under the MIT License. See LICENSE for details.


```bash

---

If you want, I can also **add a “Quick Start” section with screenshots and curl examples**, which makes it look very professional on GitHub. This is highly recommended for open-source projects.  

Do you want me to do that?

```

