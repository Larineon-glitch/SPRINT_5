from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from helpers import register_user
from data import Urls, TestUser


class TestRegistration:

    def test_successful_registration(self, driver, new_user_data):
        """Успешная регистрация"""
        driver.get(Urls.REGISTER_PAGE)
        name = new_user_data["name"]
        email = new_user_data["email"]
        password = new_user_data["password"]
        register_user(driver, name, email, password)
        WebDriverWait(driver, 5).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE

    def test_registration_error_for_short_password(self, driver, new_user_data):
        """Ошибка при коротком пароле (< 6 символов)"""
        driver.get(Urls.REGISTER_PAGE)
        name = new_user_data["name"]
        email = new_user_data["email"]
        short_password = "123"

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        assert "Некорректный пароль" in error.text