import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

l1=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
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
Ac_list=driver.find_elements(By.XPATH,"//div[@class='products']/div/h4")
print(len(Ac_list))
vegname=[]
for i in Ac_list:
    vegname.append(i.text)
print(vegname)

assert vegname == l1