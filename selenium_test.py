from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("file:///Users/falguni/Documents/DevOps/index.html")

# WAIT until element loads
wait = WebDriverWait(driver, 10)

name = wait.until(EC.presence_of_element_located((By.ID, "name")))
name.send_keys("Falguni")

driver.find_element(By.ID,"email").send_keys("falguni@gmail.com")
driver.find_element(By.ID,"password").send_keys("123456")
driver.find_element(By.ID,"confirm").send_keys("123456")

driver.find_elements(By.NAME,"gender")[0].click()

course = driver.find_element(By.ID,"course")
for option in course.find_elements(By.TAG_NAME,"option"):
    if option.text == "BCA":
        option.click()

driver.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(3)

driver.quit()