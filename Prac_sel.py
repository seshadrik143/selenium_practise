from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj_ser=Service()
optn_obj=webdriver.ChromeOptions()
optn_obj.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=obj_ser,options=optn_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Seshu")
driver.find_element(By.NAME,"email").send_keys("ram@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("ram@143")
driver.find_element(By.ID,"exampleCheck1").click()


drop=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
drop.select_by_index(1)

#driver.find_element(By.ID,"inlineRadio2").click()
radibutn=driver.find_elements(By.XPATH,"//input[@type='radio']")
radibutn[1].click()

driver.find_element(By.CSS_SELECTOR,".btn").click()
driver.find_element(By.CSS_SELECTOR,".ng-untouched").send_keys("Name Again")
