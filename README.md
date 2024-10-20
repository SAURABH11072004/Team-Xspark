# PCCOE AI Chatbot

This project involves the design and development of an AI-powered chatbot for Pimpri Chinchwad College of Engineering (PCCOE). The chatbot is built using Flask, natural language processing (NLP), and a mock database to provide users with relevant information about the college, such as admissions, scholarships, and courses.

## Features:
- Handles user queries about PCCOE through a web-based interface.
- Uses NLP for question-answering capabilities.
- Mock database integration to simulate responses related to college information.

## Tech Stack:
- **Flask**: A lightweight web framework to handle HTTP requests and serve the chatbot.
- **Transformers (NLP)**: For processing user queries and generating responses.
- **Mock Database**: Simulates storage and retrieval of college-related data.

## Setup Instructions

### 1. Environment Setup
Ensure Python and `pip` are installed, then run the following command to install the necessary libraries:

These libraries are essential for setting up the Flask app and NLP functionalities.

2. Backend Setup (Flask App)
Flask: Manages the web-based routing and user interaction.
NLP (Transformers): Processes user queries and provides intelligent responses when queries aren't found in the database.
Mock Database: Simulates storing and retrieving information about PCCOE.
3. Key Components of the Code
Flask Routes:
/: Displays a welcome message.
/chat: Accepts user queries (via a POST request), processes them, and returns a response.
NLP Model:
Uses a pre-trained question-answering model from the Transformers library to process queries that don't directly match any mock database records.
Mock Database:
Stores basic college-related data such as admissions, scholarships, and courses.
4. How It Works:
User enters a query, such as "Tell me about admissions".
The Flask app receives the query through the /chat endpoint.
The system checks the mock database for relevant information.
If no exact match is found, the NLP model generates a response.
The response is returned in JSON format and displayed to the user.
5. Example Interaction:
User Input: "Tell me about scholarships"
Chatbot Response: "Scholarships are available for merit-based and need-based students."
6. Frontend Integration (Optional)
A simple HTML page can be added for users to interact with the chatbot in real-time by entering their queries and receiving responses.

7. Deployment:
To run the chatbot locally, use the following command:

bash
flask run
The chatbot will be available at http://127.0.0.1:5000, where users can interact with it.

8. Extensions (Optional)
Add features like database logging, analytics, multi-language support, or integration with PCCOE's actual data sources for enhanced functionality.
Conclusion:
This chatbot provides a foundational AI-powered tool for answering frequently asked questions about PCCOE. It can be extended and customized as per the specific needs of the college.
```bash
pip install flask transformers
pip install flask rasa
pip install rasa
