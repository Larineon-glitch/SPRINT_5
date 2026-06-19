from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from helpers import login_user
from data import Urls


class TestLogout:

    def test_logout_from_personal_account(self, driver, existing_user):
        """Выход по кнопке «Выйти» в личном кабинете"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        login_user(driver, existing_user["email"], existing_user["password"])
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TEXT)
        )
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        )
        assert driver.current_url == Urls.LOGIN_PAGE