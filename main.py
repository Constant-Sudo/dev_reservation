import os 
from dotenv import load_dotenv
from scripts import book, links, login
from selenium.webdriver.common.by import By
from selenium import webdriver


load_dotenv()

name = os.getenv("NAME")
password = os.getenv("PASSWORD")


def main():
    driver = webdriver.Firefox()

    login.login(name, password, driver)
    


if __name__ == "__main__":
    main()
    print("Done!")