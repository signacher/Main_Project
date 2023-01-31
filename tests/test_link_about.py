from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage
from pages.client_information_page import Client_infomation_page
from pages.finish_page import Finish_page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.paymeint_page import Payment_page


def test_link_about(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Alex\\PycharmProjects\\recuorse\\chromedriver.exe',
                              chrome_options=options)

    print('\nStart test')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_menu_about()

    print('Finish test')
    # time.sleep(2 )
    # driver.quit()





