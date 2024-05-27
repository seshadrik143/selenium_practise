import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
optn=webdriver.ChromeOptions()
optn.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optn)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
veg=driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(veg))

for result in veg:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(5)

code = driver.find_element(By.CSS_SELECTOR,".promoInfo").text

assert "applied" in code
