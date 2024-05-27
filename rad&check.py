from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
optn=webdriver.ChromeOptions()
optn.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optn)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
checkboxs = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxs))

for checkbox in checkboxs:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break





