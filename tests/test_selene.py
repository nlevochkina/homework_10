from selene import by, be
from selene.support.shared.jquery_style import s


def test_selene(open_browser):
    s('.vector-search-box-input').click()
    s('.vector-search-box-input').send_keys("Программирование")
    s('.vector-search-box-input').submit()

    s(by.partial_text("Разработка программного обеспечения")).should(be.visible)
