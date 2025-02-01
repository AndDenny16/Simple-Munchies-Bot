# Davidson Commons Menu Scraper and Chatbot

(Davidson College Common's Menu, uses Jamix and doesn't allow for simple html download)
This project is a Python script that scrapes the Davidson Commons dining menu using Selenium and allows users to interact with an AI ChatBot to ask questions about the menu.

## Features
- **Scrapes** the Davidson Commons dining hall menu using Selenium.
- **Processes** the menu text and saves it to a file.
- **Chatbot** allows users to ask questions about the menu using OpenAI's GPT model.
- **Environment Variables** are used to store sensitive information.

## Requirements
Before running the script, ensure you have the following installed:
- Python 3.x
- Selenium
- OpenAI API
- LangChain
- `python-dotenv` for environment variables
- `geckodriver` for Firefox (or modify to use Chrome)

## Setup

### 1. Install Dependencies
Run the following command to install required packages:
```bash
pip install selenium openai langchain langchain-openai python-dotenv python-docx
