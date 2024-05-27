import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

obj_ser=Service()
optn_obj=webdriver.ChromeOptions()
optn_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=optn_obj,service=obj_ser)
driver.maximize_window()
driver.implicitly_wait(5)
weits=WebDriverWait(driver,10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
print(len(products))

for item in products:
    if item.find_element(By.XPATH,"div/h4/a").text == "Blackberry":
        item.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("ind")
weits.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,"//div[@class='suggestions']/ul/li/a")))

countries = driver.find_elements(By.XPATH,"//div[@class='suggestions']/ul/li/a")
print(len(countries))
for con in countries:
    if con.text == "India":

        con.click()
        break
driver.find_element(By.CSS_SELECTOR,".checkbox").click()
driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()
assert "Success!" in driver.find_element(By.CSS_SELECTOR,".alert").text

driver.close()