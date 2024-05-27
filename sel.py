import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# in this locators used to identify elements are
# ID, NAME, LINKTEXT, CLASS, XPATH, CSS SELECTOR

driver.find_element(By.NAME,"name").send_keys("Ram")
driver.find_element(By.NAME,"email").send_keys("rama@gmail.com")

# XPATH --> //tagname[@attribute='value'] --> //input[@placeholder='Password']
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("king@143")

driver.find_element(By.ID,"exampleCheck1").click()

#static drop down

drop=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
drop.select_by_index(1)
data=drop.first_selected_option.text
assert data == "Female"
drop.select_by_visible_text("Male")
dm2=drop.first_selected_option.text
assert dm2 == "Male"
#drop.select_by_visible_text("Male")
#drop.select_by_value("item") --> it is an example only
# CSS SELECTOR -->  tagname[attribute='value] --> input[type='submit']

# driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
#
# driver.find_element(By.CSS_SELECTOR,'#inlineRadio2').click() #in CSS id --> #id and class --> .class
# driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("ram Again")
# time.sleep(3)
# driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
# driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("seshu")
# message = driver.find_element(By.CLASS_NAME,"alert-success").text
# print(message)
#
# assert "Success!" in message