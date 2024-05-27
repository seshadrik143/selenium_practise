import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
optn_obj=webdriver.ChromeOptions()
optn_obj.add_experimental_option("detach",True)
optn_obj.add_argument("headless")
optn_obj.add_argument("--ignore-certificate-errors")


driver=webdriver.Chrome(service=obj_ser,options=optn_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(2)
driver.get_screenshot_as_file("sreen1.png")
