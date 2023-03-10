import pytest
from pages.auth_page import AuthPage


#  python -m pytest -v --driver Chrome --driver-path ~/chrome tests
#  python -m pytest -v --driver Chrome --driver-path /chromedriver.exe tests
import pickle
import selenium

def test_authorisation(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys('uzerovalex9@gmail.com')

    page.password.send_keys("qwerty123")

    page.btn.click()

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(page._web_driver.get_cookies(), cookies)
