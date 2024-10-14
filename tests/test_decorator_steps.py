import allure
from selene import by, be
from selene.support.shared.jquery_style import s


@allure.step("Кликаем на поле ввода")
def input_click():
    s('.vector-search-box-input').click()


@allure.step("Вводим текст в поле ввода")
def send_keys_in_input():
    s('.vector-search-box-input').send_keys("Программирование")


@allure.step("Выполняем поиск")
def do_search():
    s('.vector-search-box-input').submit()
    s(by.partial_text("Разработка программного обеспечения")).should(be.visible)


def test_decorator_steps(open_browser):
    input_click()
    send_keys_in_input()
    do_search()
