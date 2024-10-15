import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared.jquery_style import s

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'nlevochkina')
@allure.feature('Задачи в репозитории №1')
@allure.story('Пользователь может делать поиск в Википедии')
@allure.link('https://ru.wikipedia.org', name='Testing')
def test_selene(open_browser):
    s('.vector-search-box-input').click()
    s('.vector-search-box-input').send_keys("Программирование")
    s('.vector-search-box-input').submit()

    s(by.partial_text("Разработка программного обеспечения")).should(be.visible)
