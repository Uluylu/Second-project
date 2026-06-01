from selenium.webdriver.common.by import By


#HEADER
HEADER_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")                      # Кнопка перехода в Личный Кабинет в шапке
HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")                     # Кнопка возврата на главную страницу в шапке
HEADER_LOGO = (By.XPATH, "//a[@href='/']")                                              # Логотип "Stellar Burgers" в шапке для перехода на главную

#ФОРМА РЕГИСТРАЦИИ
REG_NAME_INPUT = (By.XPATH, "//div[label[text()='Имя']]/input")                         # Поле ввода Имени в форме регистрации
REG_EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input")                      # Поле ввода Логина в форме регистрации
REG_PASSWORD_INPUT = (By.XPATH, "//div[label[text()='Пароль']]/input")                  # Поле ввода Пароля в форме регистрации
REG_REGISTER_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")                    # Кнопка «Зарегистрироваться» для перехода в форму регистрации
REG_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")                 # Кнопка «Зарегистрироваться» для создания аккаунта в форме регистрации
REG_LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")                                    # Ссылка «Войти» в самом низу страницы регистрации
REG_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")                    # Текст ошибки при вводе невалидного пароля

#ФОРМА ВОССТАНОВЛЕНИЯ ПАРОЛЯ
PASS_AUTH_BUTTON = (By.XPATH, "//a[text()='Войти']")                                    # Кнопка "Войти" на форме восстановления пароля

#АВТОРИЗАЦИЯ
AUTH_EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input")                     # Поле ввода Email в форме входа (авторизации)
AUTH_PASSWORD_INPUT = (By.XPATH, "//div[label[text()='Пароль']]/input")                 # Поле ввода Пароля в форме входа (авторизации)
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")                            # Кнопка «Войти» для отправки формы авторизации

#ЛИЧНЫЙ КАБИНЕТ
PROFILE_SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")                        # Кнопка в профиле (маркер того, что Личный кабинет полностью загрузился)
PROFILE_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")                          # Кнопка деавторизации и выхода из системы внутри Личного кабинета

#ГЛАВНАЯ СТРАНИЦА И КОНСТРУКТОР
MAIN_AUTH_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")                     # Кнопка "Войти в аккаунт" на главной странице
MAIN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")                     # Кнопка на главной странице (маркер успешного входа в систему)
TAB_BUNS = (By.XPATH, "//div[span[text()='Булки']]")                                    # Вкладка переключения меню на булки
TAB_SAUCES = (By.XPATH, "//div[span[text()='Соусы']]")                                  # Вкладка переключения меню на соусы
TAB_FILLINGS = (By.XPATH, "//div[span[text()='Начинки']]")                              # Вкладка переключения меню на начинки
