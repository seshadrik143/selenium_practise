import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
name="seshu"
optn_obj=webdriver.ChromeOptions()
optn_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optn_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alert_text=alert.text
print(alert_text)

alert.accept()

# if you want to cancel use dimsis
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
alert.dismiss()