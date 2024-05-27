from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
optn_obj=webdriver.ChromeOptions()
optn_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optn_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

actn=ActionChains(driver)
actn.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
actn.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()