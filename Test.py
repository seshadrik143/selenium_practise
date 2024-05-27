import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

obj_ser=Service()
optn_obj=webdriver.ChromeOptions()
optn_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=optn_obj,service=obj_ser)
driver.get("https://chercher.tech/practice/frames")
driver.maximize_window()
driver.switch_to.frame("frame1")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys('your king')
driver.switch_to.frame("frame3")
driver.find_element(By.ID,"a").click()