import os 
from dotenv import load_dotenv
from scripts import book, links, login
from selenium.webdriver.common.by import By
from selenium import webdriver
import schedule 
import time
from datetime import datetime
from webdriver_manager.firefox import GeckoDriverManager


load_dotenv()

name = os.getenv("NAME")
password = os.getenv("PASSWORD")

running = True


def main():
    schedule.every().minute.at(":11").do(do_smth)
    
    schedule.every().day.at("00:03").do(do_smth) # Replace with login, select and book
    
    while running:
        schedule.run_pending()
        time.sleep(1)


def do_smth():
    print("I am doing something")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(current_time)


def book():
    # driver = webdriver.Firefox()
    # driver = webdriver.Firefox(executable_path="D:\Path Files\geckodriver.exe")
    # driver = webdriver.Chrome(executable_path="D:\Path Files\chromedriver.exe")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    login.login(name, password, driver)
    
    driver.close()


if __name__ == "__main__":
    book()
    print("Bye!")   