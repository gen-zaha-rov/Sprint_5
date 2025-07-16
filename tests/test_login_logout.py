from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import PageLocators
from data import UserInfo


class TestLogin:
    def test_login_user(self, driver):  # Login пользователя

        driver.get(PageLocators.homepage)

        # 1. Нажать «Вход и регистрация»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_register_button)).click()

        # 2. Заполнить все поля формы авторизации и нажать «Войти»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.email_address)).send_keys(UserInfo.valid_email)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_field)).send_keys(UserInfo.password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_button)).click()

        # 3. Проверить есть ли переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        assert WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.user_pic)).is_displayed()
        assert WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.user_name)).text == "User."


    def test_logout_user(self, driver):  # Logout пользователя

        driver.get(PageLocators.homepage)

        # 1. Нажать «Вход и регистрация»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_register_button)).click()

        # 2. Заполнить все поля формы авторизации и нажать «Войти»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.email_address)).send_keys(UserInfo.valid_email)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_field)).send_keys(UserInfo.password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_button)).click()

        # 3. Нажать кнопку «Выйти»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.logout_button)).click()

        # 4. Проверить, что в правом верхнем углу около кнопки «Разместить объявление», теперь отображается кнопка «Вход и регистрация»
        assert WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_register_button)).text == "Вход и регистрация"