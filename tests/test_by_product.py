import pytest
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
import allure
@pytest.mark.run(order=1)
@allure.description('Test buy product1')
def test_buy_product1(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Alex\\PycharmProjects\\recuorse\\chromedriver.exe', chrome_options=options)

    print('\nStart test 1')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product1()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = Client_infomation_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print('Finish test 1')
    time.sleep(2)
    driver.quit()

@pytest.mark.run(order=3)
def test_buy_product2(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Alex\\PycharmProjects\\recuorse\\chromedriver.exe', chrome_options=options)

    print('\nStart test 2')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product2()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = Client_infomation_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    print('Finish test 2')
    time.sleep(2)
    driver.quit()

@pytest.mark.run(order=2)
def test_buy_product3(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Alex\\PycharmProjects\\recuorse\\chromedriver.exe',
                              chrome_options=options)

    print('\nStart test 3')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product3()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = Client_infomation_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()
    print('Finish test 3')
    driver.quit()


