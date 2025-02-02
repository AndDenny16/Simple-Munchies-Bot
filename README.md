# Simple Davidson Dining Hall Menu Scrapper + Menu Chatbot

(Davidson College Common's Menu, uses Jamix and doesn't allow for simple html download)
This project is a Python script that scrapes the Davidson Commons dining menu using Selenium and allows users to interact with an AI ChatBot to ask questions about the menu.

Simple Example for students about how AI can Interact with Mundane Items around campus. Allows students to easily ask questions like I'm dairy free, what good do you recommend, etc

## Features
- **Scrapes** the Davidson Commons dining hall menu using Selenium. (Jamix formatting prevents simple html scrapping, have to use selenium)
- **Processes** the menu text and saves it to a file (to avoid scraping a second time for the same menu)
- **Chatbot** allows users to ask questions about the menu using OpenAI's SDK and Langchain.

## Requirements
Following installed:
- Python 3.x
- Selenium
- OpenAI SDK
- LangChain
- `geckodriver` for Firefox (or modify to use Chrome)
