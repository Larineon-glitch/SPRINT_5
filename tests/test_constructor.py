from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorPageLocators
from data import Urls


class TestConstructor:

    def test_switch_to_buns_tab(self, driver):
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
        active_tab = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert "Булки" in active_tab.text

    def test_switch_to_sauces_tab(self, driver):
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
        active_tab = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert "Соусы" in active_tab.text

    def test_switch_to_fillings_tab(self, driver):
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
        active_tab = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert "Начинки" in active_tab.text