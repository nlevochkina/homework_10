import allure
from selene import by, be
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'nlevochkina')
@allure.feature('Задачи в репозитории №3')
@allure.story('Пользователь может делать поиск в Википедии')
@allure.link('https://ru.wikipedia.org', name='Testing')
def test_decorator_steps(open_browser):
    input_click()
    send_keys_in_input()
    do_search()


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
