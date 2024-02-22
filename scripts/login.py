from scripts import links
import time
from selenium.webdriver.common.by import By
from selenium import webdriver



def login(name, password, driver):
    driver.get(links.main_login)

    driver.find_element(By.XPATH, '//*[@id="eb-base-layout-container"]/div[2]/nav/div/div/div[3]/div/div/div[1]/a').click()
    time.sleep(2)
    # Anny Forwarding
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div/div[1]/div/div/div[1]/form/div[1]/div/div/div/input').send_keys(name+"@mytum.de")
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div/div[1]/div/div/div[1]/div/button').click()
    time.sleep(2)
    # Tum Login
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div[1]/input').send_keys(name)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div[2]/input').send_keys(password)
    
    input("Ready to login?")
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div[5]/button').click()

    
    # Check for valid login
    if "anny.eu" in driver.current_url:
        print("Successfully logged in!")
    else:
        raise Exception("Login failed!")


def select(driver):
    driver.get(links.main_calendar)

    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div[3]/div[4]/div[6]/div').click()

    