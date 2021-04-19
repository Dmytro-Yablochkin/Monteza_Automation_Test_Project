from robot.libraries.BuiltIn import BuiltIn

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class SearchField_locators:
    magnifier_icon = 'css = div.site-header__search.site-header__icon'
    search_field = 'css = input.search-header__input.search__input'
    search_submit_btn = 'css = button.search-header__submit.search__submit.btn--link.site-header__icon'
    pos_search_result = '1 result for "Pulsera de Perlas del mar"'
    neg_search_result = 'Search field cannot be empty'
    # ------------------ Search data ------------------------- #
    search_data = 'Pulsera de Perlas del mar'


class SearchField:
    # 6. Check user can navigate to search result page with correct info in search field
    def search_field(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click element', SearchField_locators.magnifier_icon)

    def check_search_field(self):
        bi.run_keyword('search_field')
        bi.run_keyword('Input text', SearchField_locators.search_field, SearchField_locators.search_data)
        bi.run_keyword('Click button', SearchField_locators.search_submit_btn)
        bi.run_keyword('Wait until page contains', SearchField_locators.pos_search_result)

    # 7. "Check user can navigate to search result page with empty space in search field"
    def check_search_field_inc(self):
        bi.run_keyword('search_field')
        bi.run_keyword('Click button', SearchField_locators.search_submit_btn)
        bi.run_keyword('Wait until page contains', SearchField_locators.neg_search_result)