# Hate Speech Detection

This project is a web application that aims to detect hate speech in user comments. It's built using Python and Flask, with integration to GenAI for nuanced analysis of comments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python
- Flask
- AI/ML API(you can replace to OpenAI API, some changes required)
- Rapid API

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/hate-speech-detection.git
```
2. Navigate to the project directory
```bash
cd hate-speech-detection
```
3. Install the required packages
```bash
pip install -r requirements.txt
```
## Configuration
This project uses a config.py file for configuration, which is not included in the repository for security reasons. You will need to create your own config.py file in the root directory of the project. 
Here is a basic template for your config.py file:
```bash
# config.py

# OpenAI API Key
OPENAI_API_KEY = "your_ai/ml_api_key"
VIDEOAI_API_KEY = "your_videoai_api_key"
```
## Running the application
To run the application, execute the following command:
```bash
python app/main.py
```
