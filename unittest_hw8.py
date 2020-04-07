# Emma M | HW7 -  Unit Tests AU 3/29


import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import helpers as hp


class ChromeValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_elements_chrome(self):
        driver = self.driver
        driver.get(hp.site)
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
        text.send_keys(hp.name)
        driver.implicitly_wait(10)

        email = driver.find_element_by_xpath(hp.email_area)
        email.clear()
        email.send_keys(hp.email)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(hp.submitBtn).click()

        try:
            WebDriverWait(driver, 3) \
                .until(EC.visibility_of_element_located((By.XPATH, hp.go_back))).click()
        except NoSuchElementException:
            print("Unable to locate element")

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.img1)))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.img2)))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.img3)))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.img4)))

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page title is ", driver.title)

        driver.sleep(1)

    def test_elements_chrome_1120_550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get(hp.site)
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
        text.send_keys(hp.name)
        driver.implicitly_wait(10)

        email = driver.find_element_by_xpath(hp.email_area)
        email.clear()
        email.send_keys(hp.email)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(hp.submitBtn).click()

        try:
            WebDriverWait(driver, 3) \
                .until(EC.visibility_of_element_located((By.XPATH, hp.go_back))).click()
        except NoSuchElementException:
            print("Unable to locate element")

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.img1)))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.img2)))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.img3)))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.img4)))

        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page title is ", driver.title)

    def tearDown(self):
        self.driver.close()
