from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNavigateFromAccount:
    
    def test_click_constructor(self, authorized_main_page):        #Переход из личного кабинета в конструктор по клику на 'Конструктор
        # Переход в личный кабинет
        authorized_main_page.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        
        # Клик по кнопке "Конструктор"
        authorized_main_page.find_element(By.XPATH, "//p[text()='Конструктор']").click()
        
        # Проверка: появился заголовок "Соберите бургер"
        WebDriverWait(authorized_main_page, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))
        )
        assert authorized_main_page.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").is_displayed()
    
    def test_click_logo(self, authorized_main_page):        #Переход из личного кабинета в конструктор по клику на логотип
        # Переход в личный кабинет
        authorized_main_page.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        
        # Клик по логотипу
        authorized_main_page.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
        
        # Проверка: появился заголовок "Соберите бургер"
        WebDriverWait(authorized_main_page, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))
        )
        assert authorized_main_page.find_element(By.XPATH, "//h1[contains(text(),'Соберите бургер')]").is_displayed()