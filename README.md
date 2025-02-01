# Davidson Commons Menu Scraper and Chatbot

(Davidson College Common's Menu, uses Jamix and doesn't allow for simple html download)
This project is a Python script that scrapes the Davidson Commons dining menu using Selenium and allows users to interact with an AI ChatBot to ask questions about the menu.

## Features
- **Scrapes** the Davidson Commons dining hall menu using Selenium.
- **Processes** the menu text and saves it to a file ( to avoid scraping a second time for the same menu)
- **Chatbot** allows users to ask questions about the menu using OpenAI's GPT model.

## Requirements
Before running the script, ensure you have the following installed:
- Python 3.x
- Selenium
- OpenAI API
- LangChain
- `geckodriver` for Firefox (or modify to use Chrome)
