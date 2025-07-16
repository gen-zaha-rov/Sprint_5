from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import PageLocators
from data import UserInfo


class TestPostAd:
    def test_posting_by_unauthorized_user(self, driver):  # Размещение объявления неавторизованным пользователем

        driver.get(PageLocators.homepage)

        # 1. Нажать «Разместить объявление»
        driver.find_element(PageLocators.posting_ad_button).click()

        # 2. Проверка есть ли окно с заголовком «Чтобы разместить объявление, авторизуйтесь»
        assert WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.authorize_to_post_msg)).text == "Чтобы разместить объявление, авторизуйтесь"


    def test_posting_by_authorized_user(self, driver):  # Размещение объявления авторизованным пользователем

        driver.get(PageLocators.homepage)

        # 1. Нажать «Вход и регистрация»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_register_button)).click()

        # 2. Заполнить все поля формы авторизации и нажать «Войти»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.email_address)).send_keys(UserInfo.valid_email)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.password_field)).send_keys(UserInfo.password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.login_button)).click()

        # 3. Нажать «Разместить объявление»
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.user_pic))
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(PageLocators.posting_ad_button)).click()

        # 4. Заполнить все поля: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.product_name)).send_keys(UserInfo.name_product)
        driver.find_element(PageLocators.product_description).send_keys(UserInfo.description)
        driver.find_element(PageLocators.product_price).send_keys(UserInfo.price)

        # 5. Выбрать «Категорию» и «Город»
        driver.find_element(PageLocators.dropdown_categories).click()
        driver.find_element(PageLocators.select_categories).click()
        driver.find_element(PageLocators.dropdown_city).click()
        driver.find_element(PageLocators.select_city).click()

        # 6. Выбрать «Состояние товара»
        driver.find_element(PageLocators.product_status).click()

        # 7. Нажать «Опубликовать»
        driver.find_element(PageLocators.publish_button).click()

        # 8. Скролл вверх и переход в профиль пользователя
        driver.execute_script("window.scrollTo(0, 0);")
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.home_page))
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable(PageLocators.user_pic)).click()

        assert WebDriverWait(driver, 7).until(EC.visibility_of_element_located(PageLocators.name_product_home)).text == UserInfo.name_product