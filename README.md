# Simple Chatbot with Google Custom Search and OpenAI GPT

This is a proof-of-concept chatbot that uses the Google Custom Search Engine (CSE) to retrieve relevant web content and OpenAI's GPT-4 to generate responses. The chatbot scrapes body content from the top search results and uses it as input for the GPT model to provide a helpful answer.

## Features
- Search using Google Programmable Search Engine (CSE).
- Scrape relevant content from search result pages.
- Generate human-like responses using GPT-4 based on scraped content.
- Simple web interface using Flask.

## Prerequisites
Make sure you have the following installed:
- Python 3.7+
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for scraping
- [Requests](https://docs.python-requests.org/en/latest/) for making HTTP requests

You will also need:
- An OpenAI API key (You can get it from [OpenAI's website](https://platform.openai.com/signup/)).
- A Google Programmable Search Engine (CSE) API key and a Search Engine ID. [Follow this guide](https://developers.google.com/custom-search/v1/introduction) to create your own CSE.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/simple-chatbot.git

2. Set up a virtual environment (optional, but recommended):
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3. Install the required dependencies:
   pip install -r requirements.txt
4. Set up environment variables by creating a .env file in the project root:
   touch .env
5. Inside .env, add the following (replace with your actual keys):
   OPENAI_API_KEY=your-openai-api-key
   GOOGLE_API_KEY=your-google-api-key
   CX=your-google-cse-id

   Running the Chatbot
Run the Flask application:
   python app.py

Open your browser and go to:
   http://127.0.0.1:5000
Type your query into the input field and submit it to get a response.

How It Works
Google Search: The user's query is sent to Google Programmable Search Engine (PSE) to retrieve the top search results (URLs and snippets).
Scraping: The body content from the top results is scraped using BeautifulSoup.
AI Response: The scraped content is sent to OpenAI GPT-4 to generate a helpful and contextually relevant response.
Web Interface: The response is displayed on a simple Flask-based web page.

File Structure

.
├── app.py               # Flask app serving the chatbot interface
├── .env                 # Stores your API keys (not included in Git)
├── .gitignore           # Specifies files to ignore in Git (e.g., .env)
├── templates
│   └── index.html       # HTML template for the web interface
├── requirements.txt     # Python dependencies
└── README.md            # This README file

Dependencies
The following libraries are used in this project:

Flask: Web framework for building the chatbot interface.
OpenAI Python SDK: To interact with the GPT-4 model.
Requests: To make HTTP requests to the Google CSE API.
BeautifulSoup: For web scraping from URLs returned by Google.
Dotenv: To load environment variables from the .env file.

Contributing
Feel free to submit pull requests or report issues. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

### Instructions:

1. Replace placeholders like `your-username` and API key descriptions with actual values.
2. Save this file as `README.md` in the root of your project directory.

This `README.md` file provides clear setup instructions, describes the project, and guides other developers on how to run it.
