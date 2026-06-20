import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, RegistrationPageLocators
from data import Urls

# Генераторы данных  
def generate_email():
    names = ['test', 'ivan', 'petr', 'alex', 'maria']
    surnames = ['testov', 'ivanov', 'petrov']
    name = random.choice(names)
    surname = random.choice(surnames)
    cohort = random.randint(1, 20)
    digits = ''.join(random.choices(string.digits, k=3))
    return f"{name}_{surname}{cohort}_{digits}@yandex.ru"

def generate_password():
    length = random.randint(6, 10)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_name():
    names = ['Alexander', 'Maria', 'Dmitry', 'Elena', 'Ivan']
    return random.choice(names)

# Вспомогательные функции для тестов 
def register_user(driver, name, email, password):
    # Регистрирует пользователя 
    driver.get(Urls.REGISTER_PAGE)
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Urls.LOGIN_PAGE))

def login_user(driver, email, password):
    # Выполняет вход пользователя 
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
