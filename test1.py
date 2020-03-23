# Selenium Automation Test1 | HW6 | Emma M| 3/22/2020

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

print(driver.find_element_by_xpath("//*[@href='https://qasvus.wordpress.com/']").get_attribute("href"))      #5. Print link(href) for header message "California Real Estate"
print(driver.find_element_by_xpath("//img[@class='wp-image-55']").get_attribute("src"))                      #6. Print link(src) for first home image under "About us"
assert "California Real Estate" in driver.title                                                              #7. Verify "California Real Estate" in website title
print(driver.title)                                                                                          #8. Print website title

driver.find_element_by_class_name("accept").click()                                                          # Accept Privacy&Cookies Pop-up
driver.implicitly_wait(10)

message = driver.find_element_by_xpath("//h2[contains(text(),'Send Us a Message')]").text                    # 9. Find "Send Us a Message" and verify it's present on the web page
assert 'Send Us a Message' in message
print(message)

driver.find_element_by_id("g2-name").send_keys("Emma")      # Enter Emma in to name field
driver.find_element_by_xpath("//*[@id='g2-email']").send_keys("mukhemma@gmail.com")                           # Enter email  in to email field
driver.implicitly_wait(10)
driver.find_element_by_name("g2-message").send_keys("Hello, this is an automated message.")                   # Enter message in to message field
driver.implicitly_wait(10)
driver.find_element_by_xpath("//button[@class='pushbutton-wide']").click()                                   #click 'Submit button
driver.implicitly_wait(10)
driver.find_element_by_xpath("//a[contains(text(),'go back')]").click()                                      #click "go back" button
driver.implicitly_wait(10)
print(driver.find_element_by_class_name("pushbutton-wide").get_attribute("type"))                            #Print "typy" for Submit button

driver.close()                                                                                               #close  broswer