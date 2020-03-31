# Emma M | HW7 -  Unit Tests AU 3/29


import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

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
        email.send_keys("mukhemma@gmail.com")
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

        driver.sleep(1)

    def test_elements_chrome_1120_550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
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
        email.send_keys("mukhemma@gmail.com")
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

        driver.close()





class FirefoxValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_elements_ff(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com/')
        driver.implicitly_wait(10)

        driver.find_element_by_class_name("accept").click()
        try:
            WebDriverWait(driver, 5) \
                  .until(EC.visibility_of_element_located((By.ID, "contact-form-comment-g2-message")))
            print("TextArea is present on the page")
        except TimeoutError:
            print("Element is not found")

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page title is ", driver.title)

        driver.implicitly_wait(10)
        text = driver.find_element_by_id("g2-name")
        text.clear()
        text.send_keys("Emma")
        driver.implicitly_wait(10)

        email = driver.find_element_by_xpath("//*[@id='g2-email']")
        email.clear()
        email.send_keys("mukhemma@gmail.com")
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
        
        driver.sleep(1)

    def test_elements_ff_1250_850(self):
        driver = self.driver
        driver.set_window_size(1250, 850)
        driver.get('https://qasvus.wordpress.com/')
        driver.implicitly_wait(10)

        driver.find_element_by_class_name("accept").click()
        try:
            WebDriverWait(driver, 5) \
                  .until(EC.visibility_of_element_located((By.ID, "contact-form-comment-g2-message")))
            print("TextArea is present on the page")
        except TimeoutError:
            print("Element is not found")

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page title is ", driver.title)

        driver.implicitly_wait(10)
        text = driver.find_element_by_id("g2-name")
        text.clear()
        text.send_keys("Emma")
        driver.implicitly_wait(10)

        email = driver.find_element_by_xpath("//*[@id='g2-email']")
        email.clear()
        email.send_keys("mukhemma@gmail.com")
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

    def tearDown(self):
        self.driver.close()
