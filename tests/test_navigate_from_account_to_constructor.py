from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  
from locators import MainPageLocators
from data import Urls


class TestNavigateFromAccount:

    def test_click_constructor(self, authorized_main_page):
        # Переход из ЛК в конструктор по клику на «Конструктор» 

        # Переход в личный кабинет
        authorized_main_page.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Клик по кнопке "Конструктор"
        authorized_main_page.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        # Проверка: появился заголовок "Соберите бургер"
        assert WebDriverWait(authorized_main_page, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))
        ).is_displayed()

    def test_click_logo(self, authorized_main_page):
        # Переход из ЛК на главную по клику на логотип 

        # Переход в личный кабинет
        authorized_main_page.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Клик по логотипу
        authorized_main_page.find_element(*MainPageLocators.LOGO).click()

        # Проверка: появился заголовок "Соберите бургер"
        assert WebDriverWait(authorized_main_page, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))
        ).is_displayed()
