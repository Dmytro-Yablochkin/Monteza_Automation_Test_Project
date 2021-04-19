from robot.libraries.BuiltIn import BuiltIn

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


# LINKS

# 14. Check user can navigate to "Instagram" page
def navigate_to_inst_page():
    sl.maximize_browser_window()
    sl.scroll_element_into_view('css = #shopify-section-1583924377266 > div')
    sl.click_element('css = div.feature-row__item.feature-row__text.feature-row__text--left > a')
    sl.wait_until_page_contains('Mónteza Official (@montezaofficial)')


# 15. Check user can navigate to "Terms, Conditions, and Policies" page
def navigate_to_terms_page():
    sl.click_link('css = a[href="https://monteza.shop/pages/refund-policy"]')
    sl.wait_until_page_contains('Terms, Conditions, and Policies')


# OTHER

# 16. Check "Youtube" video block functionality
def youtube_block():
    sl.maximize_browser_window()
    sl.scroll_element_into_view('css = #shopify-section-1583925646832')
    sl.select_frame('css = div.video-wrapper iframe')
    sl.click_button('css = button.ytp-large-play-button.ytp-button')
    sl.wait_until_page_contains_element('css = div.playing-mode')