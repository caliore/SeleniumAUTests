#HW8 -  Browserstack Test 4/6/20


import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import helpers as hp

class ChromeValidation(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '80.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Sample Test'
        }

        self.driver = webdriver.Remote(
            command_executor=hp.key,
            desired_capabilities=desired_cap)

    def test_elements_chrome(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        driver.implicitly_wait(10)
        driver.find_element_by_class_name("accept").click()

        try:
            WebDriverWait(driver, 3) \
                  .until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
            print("Submit button is present on the page")
        except TimeoutError:
            print("Element is not found")

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page title is ", driver.title)

        text = driver.find_element_by_id("g2-name")
        text.clear()
        text.send_keys("Emma")
        driver.implicitly_wait(10)

        email = driver.find_element_by_xpath("//*[@id='g2-email']")
        email.clear()
        email.send_keys("test1@gmail.com")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//button[@class='pushbutton-wide']").click()

        try:
            WebDriverWait(driver, 3) \
                .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))).click()
        except NoSuchElementException:
            print("Unable to locate element")

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-55")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-34")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-56")))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wp-image-30")))

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page title is ", driver.title)

        driver.quit()
