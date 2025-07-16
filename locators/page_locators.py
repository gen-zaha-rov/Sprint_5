from selenium.webdriver.common.by import By

class PageLocators:

    # Домашняя страница
    homepage = "https://qa-desk.stand.praktikum-services.ru/"
    
    # Кнопка "Вход и регистрация"
    login_register_button = By.XPATH, "//button[text()='Вход и регистрация']"
    
    # Кнопка "Нет аккаунта"
    no_account_button = By.XPATH, "//button[text()='Нет аккаунта']" 
    
    # Поле "Email"
    email_address = By.CSS_SELECTOR, "input[name='email']" 

    # Поле "Пароль"
    password_field = By.CSS_SELECTOR, "input[name='password']"

    # Поле "Повторите пароль"
    password_confirm = By.NAME, "submitPassword"

    # Кнопка "Создать аккаунт"
    create_account_button = By.XPATH, "//button[text()='Создать аккаунт']"

    # Поле "Email" подсвечено красным
    email_field_error = By.XPATH, "(//div[contains(@class, 'input_inputError')])[1]"

    # Поле "Пароль" подсвечено красным
    password_field_error = By.XPATH, "(//div[contains(@class, 'input_inputError')])[2]"

    # Поле "Повторите пароль" подсвечено красным
    confirm_password_field_error = By.XPATH, "(//div[contains(@class, 'input_inputError')])[3]"

    # Сообщение об ошибке под полем email
    email_error_message = By.XPATH, "//span[text()='Ошибка']"

    # Аватар пользователя (при успешной регистрации)
    user_pic = By.XPATH, '//button[@class="circleSmall"]'

    # Имя пользователя (при успешной регистрации)
    user_name = By.XPATH, "//h3[@class='profileText name']"    
    
    # Кнопка "Разместить объявление"
    posting_ad_button = By.XPATH, "//*[text()='Разместить объявление']"

    # Кнопка "Войти"
    login_button = By.XPATH, "//button[text()='Войти']"

    # Кнопка "Выйти"
    logout_button = By.XPATH, "//button[text()='Выйти']"

    # Окно «Чтобы разместить объявление, авторизуйтесь»
    authorize_to_post_msg = By.XPATH, "//h1[@class='h1']" 

    # Название товара
    product_name = By.XPATH, "//input[@name='name']"

    # Описание товара
    product_description = By.XPATH, "//textarea[@name='description']"

    # Стоимость товара
    product_price = By.XPATH, "//input[@name='price']"

    # Dropdown "Город"
    dropdown_city = By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[2]"

    # Выбор города (Новосибирск)
    select_city = By.XPATH, "//span[text()='Новосибирск']"

    # Dropdown "Категории"
    dropdown_categories = By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[1]"

    # Выбор категории (Хобби)
    select_categories = By.XPATH, "//span[text()='Хобби']"

    # RabioButton "Состояние товара" Б/У
    product_status = By.XPATH, "//div[contains(@class, 'radioUnput_inputRegular')]"

    # Кнопка "Опубликовать"
    publish_button = By.XPATH, "//button[text()='Опубликовать']"

    # Прогрузка профиля
    home_page = By.XPATH, "//*[contains(@class, 'homePage_homepage')]"

    # Название объявления в разделе "Мои объявления"
    name_product_home = By.XPATH, "//h2[text()='Воздушный змей']"