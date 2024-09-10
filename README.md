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
   cd simple-chatbot
