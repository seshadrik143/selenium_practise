from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
optn_obj=webdriver.ChromeOptions()
optn_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optn_obj)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Click Here").click()
webpages=driver.window_handles
driver.switch_to.window(webpages[1])
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
driver.close()

driver.switch_to.window(webpages[0])
assert "Opening a new window" == driver.find_element(By.CSS_SELECTOR,"h3").text
