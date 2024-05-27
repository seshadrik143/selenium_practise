import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
optin=webdriver.ChromeOptions()
optin.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optin)
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com") # paren to child using Xpath
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("hello@12345") # paren to child using CSS
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("hello@12345")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
