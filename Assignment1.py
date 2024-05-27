import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_ser=Service()
optn_obj=webdriver.ChromeOptions()
optn_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=obj_ser,options=optn_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR,"a[class='blinkingText']").click()
windws=driver.window_handles
driver.switch_to.window(windws[1])
time.sleep(2)

data=driver.find_element(By.XPATH,"//p[text()='Please email us at ']").text

print(data)
sd_data= data.split()
print(sd_data)
ac_mail=[]
for mail in sd_data:
    if mail == driver.find_element(By.XPATH,"//a[text()='mentor@rahulshettyacademy.com']"):
       ac_mail=mail
       break
print(ac_mail)