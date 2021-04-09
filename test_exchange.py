from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'webdriver/chromedriver')
driver.maximize_window()
driver.get("https://changenow.io/exchange")
wallet_input = driver.find_element_by_id("recipientWallet")
wallet_input.send_keys("0xC257274276a4E539741Ca11b590B9447B26A8051")
exchange_button_next = driver.find_element_by_class_name("exchange-stepper--next-button")
exchange_button_next.click()
confirm_button = driver.find_element_by_class_name("now-button__green")
confirm_button.click()
