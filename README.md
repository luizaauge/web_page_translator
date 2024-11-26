# Web Page Translator

This project extracts text content from a given URL, translates it to a specified language using the Microsoft Translator API, and saves the translated text to a file named `translated_page.md`.

## Features
- Extracts text content from web pages.
- Translates the extracted text to a specified language.
- Saves the translated text to a file.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Install the required libraries:
   ```bash
    pip install requests beautifulsoup4

## Usage

1. Update the `subscription_key`, `endpoint`, and `location` variables in main.py with your Microsoft Translator API credentials.

2. Run the script:
    ```bash
    python main.py

3. The translated text will be saved to translated_page.md.

## Functions
`extract_text(url)`
Extracts and returns the text content from the given URL.

Args:
- `url (str)`: The URL of the web page to extract text from.

Returns:
- `str`: The extracted text content.


`translator(text, target_language)`
Translates the given text to the specified target language using the Microsoft Translator API.

Args:
- `text (str)`: The text to translate.
- `target_language (str)`: The target language code (e.g., pt-br for Brazilian Portuguese).

Returns:
- `str`: The translated text.


`translate_url(url, target_language)`
Extracts text from the given URL, translates it to the specified target language, and saves the translated text to translated_page.md.

Args:
- `url (str)`: The URL of the web page to extract and translate text from.
- `target_language (str)`: The target language code.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
