import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

obj_ser=Service()
optin_obj=webdriver.ChromeOptions()
optin_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optin_obj)
driver.maximize_window()
driver.implicitly_wait(5)
wehts=WebDriverWait(driver,10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
#time.sleep(1)
wehts.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products div.product")))


veg=driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(veg))

for result in veg:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

amount=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for result in amount:
    sum= sum+ int(result.text)

total_amount= int((driver.find_element(By.XPATH,"//span[@class='totAmt']").text))
assert sum == total_amount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

wehts.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoCode")))
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

code = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(code)

assert "applied" in code

ac_amount=int((driver.find_element(By.CSS_SELECTOR,".totAmt").text))
print(ac_amount)
dc_amount=float((driver.find_element(By.CSS_SELECTOR,".discountAmt").text))
print(dc_amount)
assert ac_amount>dc_amount