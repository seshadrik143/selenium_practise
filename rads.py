from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
optn=webdriver.ChromeOptions()
optn.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optn)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
rads=driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(rads))
for radio in rads:
    if radio.get_attribute("value") == "radio3":
        radio.click()
        assert radio.is_selected()
        break


assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert driver.find_element(By.ID,"displayed-text").is_displayed()

