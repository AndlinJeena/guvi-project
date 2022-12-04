from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
class Orange:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Firefox()
 
    def login(self):
        username = "flowerrose"
        password = "Flower#123#rose"
 
        username_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'  
        password_xpath='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        login_button_xpath='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
 
        self.driver.get(self.url)
        time.sleep(5)
 
        username_xpath = self.driver.find_element(by=By.XPATH, value=username_xpath)
        password_xpath = self.driver.find_element(by=By.XPATH, value=password_xpath)
        login_button_xpath=self.driver.find_element(by=By.XPATH, value=login_button_xpath)
 
        username_xpath.send_keys(username)
        password_xpath.send_keys(password)

        time.sleep(3)

        login_button_xpath.click()
 
o=Orange()
 
o.login()
