import allure
from selene import by, be
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'nlevochkina')
@allure.feature('Задачи в репозитории №2')
@allure.story('Пользователь может делать поиск в Википедии')
@allure.link('https://ru.wikipedia.org', name='Testing')
def test_selene():
    with allure.step("Кликаем на поле ввода"):
        s('.vector-search-box-input').click()

    with allure.step("Вводим текст в поле ввода"):
        s('.vector-search-box-input').send_keys("Программирование")

    with allure.step("Выполняем поиск"):
        s('.vector-search-box-input').submit()
        s(by.partial_text("Разработка программного обеспечения")).should(be.visible)
