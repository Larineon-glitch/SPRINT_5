from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка "Личный кабинет" в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка "Конструктор" в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип Stellar Burgers
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    # Кнопка "Оформить заказ" (признак авторизации)
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

class LoginPageLocators:
    # Поле Email
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])")
    # Поле Пароль
    PASSWORD_INPUT = (By.NAME, "Пароль")
    # Кнопка "Войти"
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")
    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class RegistrationPageLocators:
    # Поле Имя
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")
    # Поле Email
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    # Поле Пароль
    PASSWORD_INPUT = (By.NAME, "Пароль")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Сообщение об ошибке
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'пароль')]")
    # Ссылка "Войти" на странице регистрации
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

class ProfilePageLocators:
    # Кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # Текст в личном кабинете
    PROFILE_TEXT = (By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")

class ForgotPasswordPageLocators:
    # Кнопка "Войти" на странице восстановления пароля
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")

class ConstructorPageLocators:
    # Табы
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Активный таб
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")