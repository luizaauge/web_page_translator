import os
import requests
from bs4 import BeautifulSoup


def extract_text(url):
    """
    Extracts and prints the text content from the given URL.

    Args:
        url (str): The URL of the web page to extract text from.
    """
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()
        title = soup.title.string if soup.title else 'No Title Found'
        paragraphs = soup.find_all('p')
        body = '\n\n'.join([para.get_text(separator=' ') for para in paragraphs])
        text = f"{title}\n\n{body}"
        return text
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None


subscription_key = "your_subscription_key"
endpoint = 'your_endpoint'
location = 'your_location'
to_language = 'your_to_language'


def translator(text, target_language):
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': target_language
    }

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(os.urandom(16))
    }

    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body, timeout=10)
    response = request.json()
    return response[0]['translations'][0]['text']


def translate_url(url, target_language):
    text = extract_text(url)
    translated_text = translator(text, target_language)
    with open('article.md', 'w', encoding='utf-8') as file:
        file.write(translated_text)
    print(f"Translated text written to {'article.md'}")


translate_url("https://medium.com/mit-initiative-on-the-digital-economy/data-ownership-and-privacy-protection-spark-new-debates-9a8b79f4255f", "pt-br")
