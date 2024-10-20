## Team Name:Team Xspark 

## Team ID:21


## Problem Statement Title:Design and Develop an AI-Powered Chatbot for PCCOE


## Description:
The PCCOE AI Chatbot project aims to streamline the query-handling process for Pimpri Chinchwad College of Engineering (PCCOE) by providing an AI-driven chatbot system. This chatbot uses **Flask** for its web interface and **Natural Language Processing (NLP)** for intelligent query handling. By leveraging a **mock database**, the chatbot can provide quick and accurate information related to PCCOE, including details on admissions, scholarships, and courses. If the information is not available in the database, an **NLP-based fallback system** generates appropriate responses, ensuring the user query is handled efficiently.

The chatbot is designed to assist students, faculty, and prospective students by addressing frequently asked questions (FAQs) about the college, making the process more user-friendly and reducing manual efforts in responding to repetitive inquiries.

## Features:
- **Web-Based Interface**: A simple and intuitive interface where users can interact with the chatbot via a web browser.
- **NLP-Based Query Processing**: Utilizes NLP models to interpret user queries and provide relevant responses.
- **Mock Database**: Simulates a database containing basic information about PCCOE, such as admissions procedures, available scholarships, and offered courses.
- **Fallback Mechanism**: For queries not directly handled by the mock database, the chatbot uses an NLP fallback to generate meaningful answers.
- **Extensibility**: Built with a modular architecture, the chatbot can be extended to integrate with actual PCCOE databases or include additional features like multi-language support and data logging.

## Tech Stack:
- **Flask**: A lightweight and flexible Python web framework for handling HTTP requests, user input, and routing.
- **Transformers (NLP)**: Provides powerful pre-trained models to process and understand natural language queries.
- **Mock Database**: A simulated in-memory database storing basic college-related information.
- **Rasa**: An open-source machine learning framework for automated text and voice-based conversations, used for advanced chatbot conversation handling and dialogue flow.

## Screenshots:
### Chatbot Interface:
![Screenshot 2024-10-20 195421](https://github.com/user-attachments/assets/68af7364-135b-4034-bbd5-a33681f29244)
![Screenshot 2024-10-20 195502](https://github.com/user-attachments/assets/db6f3bb6-7716-4a5c-8a27-cb6cb2f7ff29)
![Screenshot 2024-10-20 195547](https://github.com/user-attachments/assets/e5919a64-3859-45fe-bd65-f02ded469fbd)


## Deployed URL:![Uploading Screenshot 2024-10-20 195547.png…]()

The chatbot is deployed and can be accessed at the following link:  
[Deployed Solution](https://drive.google.com/drive/folders/1EeP97ghh-AMtpyh9lQ64rJiHbqMhZGtc?dmr=1&ec=wgc-drive-hero-goto)

## Video URL:
A demo video showcasing the chatbot in action can be viewed here:  
[Demo Video](https://drive.google.com/drive/folders/1EeP97ghh-AMtpyh9lQ64rJiHbqMhZGtc?dmr=1&ec=wgc-drive-hero-goto)

## Run Commands:
To set up and run the chatbot locally, follow these steps:
   ```bash
pip install flask transformers
pip install flask rasa
pip install rasa
python app.py

  
