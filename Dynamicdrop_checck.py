import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
optn_obj=webdriver.ChromeOptions()

optn_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=optn_obj,service=obj_ser)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("Ind")
time.sleep(2)
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break


# validation using assert
# for dynamic text updation you will not get text using .text method instead use get attribute

assert driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute("value") == "India"


