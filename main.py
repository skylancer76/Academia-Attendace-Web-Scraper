from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

login_url = "https://academia.srmist.edu.in"
scrape_url = "https://academia.srmist.edu.in/#Page:My_Attendance"

email = input("Enter your Email ID :")
password = input("Enter your Password :")

driver = webdriver.Chrome()

driver.get(login_url)
time.sleep(3)

driver.switch_to.frame("zohoiam")

try:
    username_field = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.XPATH, "//*[@id='login_id']"))
    )
    username_field.send_keys(email) 
except Exception as e:
    print(f"An error occurred: {e}")

nextbtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='nextbtn']")))
nextbtn.click()
time.sleep(3)

try:
    password_field = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.NAME, "PASSWORD"))
    )
    password_field.send_keys(password) 
except Exception as e:
    print(f"An error occurred: {e}")

sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='nextbtn']")))
sign_in_button.click()
time.sleep(3)

driver.switch_to.default_content()
WebDriverWait(driver, 10).until(EC.url_contains("WELCOME"))

menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hiddendMenu']"))).click()

myTimeTableBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hiddendMenu']/div/ul/li[1]"))).click()
time.sleep(3)

attendanceBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hiddendMenu']/div/ul/li[1]/div/ul/li[2]"))).click()
WebDriverWait(driver, 10).until(EC.url_contains("My_Attendance"))
time.sleep(3)

subjects = driver.find_elements(By.XPATH, "//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div/table[3]/tbody/tr")

for sub in subjects:
    print(sub.text)

driver.quit()
