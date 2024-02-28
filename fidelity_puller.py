from time import sleep
from os import environ as envvar
from selenium.webdriver.common.by import By
import undetected_chromedriver as chromedriver


def log_in(fidelity):
    fidelity.get('https://nb.fidelity.com/public/nb/intel/home')
    username, password = envvar['fidelity_username'], envvar['fidelity_password']
    username_box = fidelity.find_element(By.XPATH, "//input[@id='ssnt']")
    password_box = fidelity.find_element(By.XPATH, "//input[@id='pin']")
    login_button = fidelity.find_element(By.XPATH, "//input[@title='Log In']")
    username_box.send_keys(username)
    password_box.send_keys(password)
    login_button.click()
    sleep(10)



if __name__ == '__main__':
    driver = chromedriver.Chrome()
    log_in(driver)
