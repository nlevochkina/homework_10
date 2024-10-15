import allure
from allure_commons.types import Severity


def test_steps():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'nlevochkina')
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Пользователь может делать поиск в Википедии')
    allure.dynamic.link('https://ru.wikipedia.org', name='Testing')
    pass


def test_selene():
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'nlevochkina')
@allure.feature('Задачи в репозитории')
@allure.story('Пользователь может делать поиск в Википедии')
@allure.link('https://ru.wikipedia.org', name='Testing')
def test_decorator_steps():
    pass
