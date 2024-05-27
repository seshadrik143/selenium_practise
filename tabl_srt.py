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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.LINK_TEXT,"Top Deals").click()
pages=driver.window_handles
driver.switch_to.window(pages[1])
browswer_sorted_list=[]
driver.find_element(By.CSS_SELECTOR,"span[class='sort-icon sort-descending']").click()
time.sleep(1)
vegnames1=driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
for veg in vegnames1:
    browswer_sorted_list.append(veg.text)

originallist= browswer_sorted_list.copy()

browswer_sorted_list.sort()

print(browswer_sorted_list)
print(originallist)

assert browswer_sorted_list == originallist
