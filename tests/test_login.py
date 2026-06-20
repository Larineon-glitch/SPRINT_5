from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators
from helpers import login_user
from data import Urls


class TestLogin:

    def test_login_main_button(self, driver, existing_user):
        """Вход по кнопке «Войти в аккаунт» на главной"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        login_user(driver, existing_user["email"], existing_user["password"])
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert driver.current_url == Urls.MAIN_PAGE

    def test_login_personal_account_button(self, driver, existing_user):
        """Вход через кнопку «Личный кабинет»"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        login_user(driver, existing_user["email"], existing_user["password"])
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert driver.current_url == Urls.MAIN_PAGE

    def test_login_registration_form_link(self, driver, existing_user):
        """Вход через кнопку в форме регистрации"""
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()
        login_user(driver, existing_user["email"], existing_user["password"])
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert driver.current_url == Urls.MAIN_PAGE

    def test_login_forgot_password_form_link(self, driver, existing_user):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(Urls.FORGOT_PASSWORD_PAGE)
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON).click()
        login_user(driver, existing_user["email"], existing_user["password"])
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert driver.current_url == Urls.MAIN_PAGE