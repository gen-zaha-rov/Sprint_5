from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import PageLocators
from data import UserInfo
from faker import Faker


class TestRegistration:
    # тесты на функциональность «Регистрация пользователя»

    def test_successful_signup(self, driver):  # Регистрация пользователя прошла успешно
        fake = Faker('en_US')

        driver.get(PageLocators.homepage)

        # 1. Нажать «Вход и регистрация»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_register_button)).click()

        # 2. Нажать «Нет аккаунта»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.no_account_button)).click()

        # 3. Заполнить поля регистрации и нажать «Создать аккаунт»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.email_address)).send_keys(fake.email())
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_field)).send_keys(UserInfo.password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_confirm)).send_keys(UserInfo.password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.create_account_button)).click()

        # 4. Проверка успешности регистрации: есть ли переход на домашнюю страницу, где выводится аватар пользователя и имя User.
        assert WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.user_pic)).is_displayed()
        assert WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.user_name)).text == "User."


    def test_signup_with_invalid_email(self, driver):  # Регистрация пользователя с заведомо некорректным email
        
        driver.get(PageLocators.homepage)

        # 1. Нажать «Вход и регистрация»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_register_button)).click()

        # 2. Нажать «Нет аккаунта»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.no_account_button)).click()

        # 3. Заполнить поля регистрации и нажать «Создать аккаунт»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.email_address)).send_keys(UserInfo.not_valid_email)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_field)).send_keys(UserInfo.password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_confirm)).send_keys(UserInfo.password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.create_account_button)).click()

        # 4. Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка»
        email_error = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.email_field_error))
        password_error = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_field_error))
        confirm_password_error = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.confirm_password_field_error))

        assert email_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert confirm_password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert driver.find_element(PageLocators.email_error_message).text == "Ошибка"


    def test_register_existing_user(self, driver):  # Регистрация уже существующего пользователя

        driver.get(PageLocators.homepage)

        # 1. Нажать «Вход и регистрация»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_register_button)).click()

        # 2. Нажать «Нет аккаунта»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.no_account_button)).click()

        # 3. Заполнить поля регистрации и нажать «Создать аккаунт»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.email_field)).send_keys(UserInfo.valid_email)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_field)).send_keys(UserInfo.password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.confirm_password_field)).send_keys(UserInfo.password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.create_account_button)).click()

        #4. Проверить поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка»
        email_error = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.email_field_error))
        password_error = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_field_error))
        confirm_password_error = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.confirm_password_field_error))

        assert email_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert confirm_password_error.value_of_css_property("border") == '0.8px solid rgb(255, 105, 114)'
        assert driver.find_element(PageLocators.email_error_message).text == "Ошибка"
