from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from helpers import login_user
from data import Urls


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver, existing_user):
        #Переход в личный кабинет по клику 
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
        assert driver.current_url == Urls.ACCOUNT_PAGE

    def test_go_from_personal_account_to_constructor(self, driver, existing_user):
        #Переход из ЛК в конструктор по кнопке «Конструктор» 
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
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert driver.current_url == Urls.MAIN_PAGE

    def test_go_from_personal_account_to_main_via_logo(self, driver, existing_user):
        #Переход из ЛК на главную через логотип
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
        driver.find_element(*MainPageLocators.LOGO).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert driver.current_url == Urls.MAIN_PAGE