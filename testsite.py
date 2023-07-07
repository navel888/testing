import selenium.webdriver.chrome.options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'
id_login = 'user-name'
id_password =  'password'
id_login_button =  'login-button'


chrome_options = selenium.webdriver.chrome.options.Options()
chrome_options.add_argument("--window-size=1920,800")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(10)
driver.get(URL)

input_login = driver.find_element(By.ID, id_login)
input_password = driver.find_element(By.ID, id_password)
input_login.send_keys(LOGIN)
input_password.send_keys(PASSWORD)

login_button = driver.find_element(By.ID, id_login_button)
login_button.click()


driver.quit()