from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from openai import OpenAI
import time
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import docx
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

ORGANIZATION = os.getenv("ORGANIZATION")
API_KEY = os.getenv("OPEN_AI_API")
PROJECT = os.getenv("PROJECT")
SELENIUM_DRIVER = os.getenv("DRIVER_PATH")
DAVIDSON_MENU = os.getenv("DAVIDSON_MENU")
FILE = os.getenv("FILE")


client = OpenAI(
    organization = ORGANIZATION,
    project = PROJECT,
    api_key = API_KEY
)

def chatbot(menutext):
    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Given this list of ingredients at the dining hall at Davidson Commons. Answer the following questions about the food options:" + menutext),
        MessagesPlaceholder("history"),
        ("human", "{question}")
    ])

    chain = prompt | llm 
    user_input = input("What do you wanna know? (Type 'Exit' to quit): ")
    history = []
    while user_input.lower() != "exit":
        response = chain.invoke({"history": history, "question": user_input})
        history.append(("human", user_input))
        history.append(("ai", response.content))
        print(response.content)
        user_input = input("What do you wanna know? (Type 'Exit' to quit): ")
    


def setup():
    #Creating the Driver
    service = Service(SELENIUM_DRIVER)
    driver = webdriver.Firefox(service=service)
    return driver

def pull(driver):
    driver.get(DAVIDSON_MENU)
    wait = WebDriverWait(driver,70)
    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.v-button.v-widget.multiline.v-button-multiline.selection.v-button-selection.icon-align-right.v-button-icon-align-right.v-has-width')))
    button.click()
    currentHour = time.localtime().tm_hour
    if (currentHour > 13 ):
        element = wait.until(EC.element_to_be_clickable((By.ID, "gwt-uid-2")))
    else:
        element = wait.until(EC.element_to_be_clickable((By.ID, "gwt-uid-3")))

    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(1) 
    element.click()

    span_elements = driver.find_elements(By.CLASS_NAME, 'v-button-caption')
    titles = driver.find_elements(By.CLASS_NAME, "multiline-button-caption-text")
    print(len(span_elements))
    titles_list = []
    for title in titles:
        titles_list.append(title.text)
    span_elements2 = span_elements[5:]
    string_output = ''
    for i in range(len(titles_list)):
        string_output +=  "In the " + titles_list[i] +  " Category Today Commons is serving: \n"
        string_output += span_elements2[i].text + " \n"
    return string_output

def write(path, string_text):
    #Saving The Commons Menu Information in a Text Document
    try: 
        with open(path,"w") as file1: 
            file1.write(string_text)
            file1.close()
    except FileNotFoundError:
        print('File Not Found')


def main():
    decider = input("Mode (Y for Scrapping, N if you already have the todays menu): " ) 
    if (decider == "Y"):
        driver = setup()
        text = pull(driver)
        write("foodtoday.txt", text)
    else:
        file = open("foodtoday.txt", "r")
        text = file.read()
    chatbot(text)


if __name__ == "__main__":
    main()
