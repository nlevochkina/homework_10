import allure
from selene import by, be
from selene.support.shared.jquery_style import s


def test_selene():

    with allure.step("Кликаем на поле ввода"):
        s('.vector-search-box-input').click()

    with allure.step("Вводим текст в поле ввода"):
        s('.vector-search-box-input').send_keys("Программирование")

    with allure.step("Выполняем поиск"):
        s('.vector-search-box-input').submit()
        s(by.partial_text("Разработка программного обеспечения")).should(be.visible)
