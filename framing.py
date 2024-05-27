import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

obj_ser=Service()
optn_obj=webdriver.ChromeOptions()
optn_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optn_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Testing frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)