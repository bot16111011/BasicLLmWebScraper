# AI Web Scraper

A Python-based AI web scraper that uses Streamlit for the front-end interface and Selenium for web scraping. This tool enables users to scrape website content, clean and parse it based on a description, and retrieve specific information using a language model.

## Features

- **Scraping Website Content**: Fetches content from a specified URL using Selenium.
- **Content Cleaning**: Cleans the scraped HTML content by removing scripts and styles, leaving only the relevant text.
- **DOM Content Parsing**: Uses a custom parsing function that interprets the content based on user input, leveraging the Ollama language model.
- **Streamlit Interface**: Provides a simple and interactive interface to enter URLs and retrieve parsed content.

## Requirements

To run this project, you need the following dependencies:

- `streamlit`
- `selenium`
- `beautifulsoup4`
- `langchain_ollama`
- `langchain_core`
  
Install the requirements using:
```bash
pip install -r requirements.txt
```

## Usage

1. **Enter the Website URL**: Launch the Streamlit app and enter the URL of the website you want to scrape.
2. **Scrape the Website**: Click the "Scrape Site" button. The tool will display the DOM content in a text area for review.
3. **Describe Content to Parse**: Enter a description of the specific information you wish to extract.
4. **Parse the Content**: Click "Parse Content" to parse the DOM content based on the description, and view the result.

### Example

After entering a website URL and a description like "Extract all product names," the application will parse the cleaned content and display only the relevant information.

## Project Structure

- **main.py**: Contains the Streamlit interface and links the scraping and parsing functionalities.
- **scrape.py**: Handles web scraping using Selenium and processes the DOM content (cleaning and extraction).
- **parse.py**: Includes parsing logic with the Ollama language model for content extraction based on user-provided descriptions.

## Files

- **main.py**: The main entry point for the Streamlit app.
- **scrape.py**: Defines functions for scraping and cleaning website content.
- **parse.py**: Handles parsing content with a language model based on a user-defined description.

## Configuration

- **API Key**: Replace `AUTH` in `scrape.py` with your API key for secure scraping access.

## To Do

- **Error Handling**: Add error handling for invalid URLs and parsing errors.
- **Parsing Improvements**: Enhance parsing to handle more complex DOM structures.
- **Model Customization**: Add configuration options for different language model parameters if needed.

## Running the Project

Run the application with:
```bash
streamlit run main.py
```
## Notes
Ensure the necessary API key is set in the scrape.py file, and confirm that all required dependencies are installed.

1. **Error Handling**: Add error handling for invalid URLs and parsing exceptions to make the tool more robust.
2. **User Feedback on Parsing**: Show a loading spinner or some feedback message while the scraping/parsing process is in progress, especially for larger sites.
3. **Logging**: Add logging for debugging and tracking, especially within `scrape.py`.
4. **API Key Handling**: Store your API key in a secure configuration file or environment variable rather than hardcoding it.


