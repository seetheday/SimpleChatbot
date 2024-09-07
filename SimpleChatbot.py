import requests
import openai
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CX = os.getenv("CX")

# Set up your OpenAI API key
openai.api_key = OPENAI_API_KEY

# Google Custom Search Engine (PSE) configuration


def google_search(query, num_results=5):
    """
    Function to query Google Custom Search API (Programmable Search Engine)
    and return the top search result URLs and snippets.
    """
    search_url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": CX,
        "q": query,
        "num": num_results,  # Number of search results to retrieve
    }

    response = requests.get(search_url, params=params)
    response.raise_for_status()

    data = response.json()

    # Extract URLs and snippets from the search results
    results = []
    if "items" in data:
        for item in data["items"]:
            url = item.get("link", "")
            snippet = item.get("snippet", "")
            results.append({"url": url, "snippet": snippet})
    return results

def scrape_website(url):
    """
    Function to scrape the body text from the provided URL.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        page = requests.get(url, headers=headers)
        page.raise_for_status()  # Raise an exception if the request fails

        soup = BeautifulSoup(page.content, "html.parser")

        # Extract the body text or main content from the page
        paragraphs = soup.find_all("p")  # Assuming main content is within <p> tags
        text = "\n\n".join([p.get_text() for p in paragraphs])
        return text
    except requests.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return ""

def generate_ai_response(user_query, combined_content):
    """
    Generate a response using GPT-4, given the user's query and the scraped content.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"User asked: '{user_query}'. Here is some relevant content: '{combined_content}'. Please generate a helpful answer for the user."}
    ]

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=2000  # Adjust the response length as needed
    )

    return response.choices[0].message.content.strip()

def main():
    user_query = "how do I check my claim status?"

    # Step 1: Get the top Google search results (fetching 2 results)
    search_results = google_search(user_query, num_results=2)

    # Step 2: Scrape the body content from each URL
    scraped_content = []
    for result in search_results:
        url = result["url"]
        snippet = result["snippet"]
        print(f"Scraping URL: {url}")
        full_text = scrape_website(url)
        if full_text:
            # Combine the snippet and full text for richer content
            combined_text = f"{snippet}\n\n{full_text}"
            scraped_content.append(combined_text)

    # Combine all scraped content into a single string
    combined_content = "\n\n".join(scraped_content)

    # Step 3: Generate a response using GPT-4 and the scraped content
    if combined_content.strip():
        ai_response = generate_ai_response(user_query, combined_content)
        print(f"AI Chatbot Response:\n{ai_response}")
    else:
        print("No content available from search results.")

if __name__ == "__main__":
    main()