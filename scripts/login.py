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
    
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div[5]/button').click()

    # Check for valid login
    # if "anny.eu" in driver.current_url:
    #     print("Successfully logged in!")
    # else:
    #     raise Exception("Login failed!")
    
    # Wait until the page has loaded
    driver.implicitly_wait(5)

    select(driver)


def select(driver):
    
    #NOTE Wait until fully loaded
    
    # Looking with title
    # val = "Wednesday, March 13, 2024"
    
    elem = driver.find_element(By.NAME, "Tuesday, March 12, 2024")
    # elem = driver.find_element(By.XPATH, '//a[@title="Tuesday, March 12, 2024"]')
    
    # Looking with XPATH
    # elem = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div[2]')
    
    js_code = "arguments[0].scrollIntoView();"
    driver.execute_script(js_code, elem)
    # time.sleep(2)
    elem.click() 
    
    day_title = "Monday, March 11, 2024" #NOTE dynamic date
    # elem = driver.find_element(By.XPATH, f"//a[@title='{day_title}']")

    
    # Start Time
    elem = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/ul/li[6]')
    # time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", elem)
    # time.sleep(1)
    elem.click()



    # End Time 
    elem = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[8]')
    # time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", elem)
    # time.sleep(1)
    elem.click()
    # Print out seat count
    # seats = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/div/span').text()
    seats = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/div/span')
    print(seats)

    # Book
    # elem = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/button[2]/span[1]/span')
    # time.sleep(1)
    # driver.execute_script("arguments[0].scrollIntoView();", elem)
    # time.sleep(1)
    # elem.click()

    return 