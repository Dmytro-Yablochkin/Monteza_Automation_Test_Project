from robot.libraries.BuiltIn import BuiltIn

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class AppForm_locators:
    app_btn = 'css = button.bcontact-trigger-button'
    name_field = 'css = #bcontact-name'
    email_field = 'css = #bcontact-email'
    address_field = 'css = #bcontact-custom_1606480215797'
    inst_name_field = 'css = #bcontact-custom_1606480317240'
    flwrs_field = 'css = #bcontact-custom_1606480318969'
    hear_about_checkbox = 'css = label[for="bcontact-custom_1606480320478--My PR Manager"]'  # PR-Manager
    agree_checkbox = 'css = label[for="bcontact-custom_1606480321994--Yes"]'  # Yes
    question_checkbox = 'css = label[for="bcontact-custom_1606480573112--Earrings"]'  # Earrings
    brief_field = 'css = #bcontact-custom_1606484269050'
    app_submit_btn = 'css = .bcontact-submit--right > button'
    challenge_message = 'css = p.shopify-challenge__message'
    # -------------------- User correct data ---------------------------- #
    app_user_name = 'John Smith'
    app_user_email = 'test@test.com'
    app_user_address = 'Boston, Massachusetts, USA, 02108'
    app_user_inst_name = '@john13smith'
    app_user_flwrs = '1500'
    brief_text = 'Very good jewelry web-shop'
    # ------------------ User incorrect data ---------------------------- #
    app_user_inc_name = '123456'
    app_user_inc_email = 'test@est.com'
    app_user_inc_address = 'Boston'
    app_user_inc_inst_name = 'john'
    app_user_inc_flwrs = '-150'


class AppForm:
    # 17. Check user can submit "Ambassador application form" with correct data
    def ambassador_app_form(self):
        sl.maximize_browser_window()
        bi.run_keyword('Wait until element is visible', AppForm_locators.app_btn)
        bi.run_keyword('Click button', AppForm_locators.app_btn)

    def submit_ambassador_appform(self):
        bi.run_keyword('ambassador_app_form')
        bi.run_keyword('Input text', AppForm_locators.name_field, AppForm_locators.app_user_name)
        bi.run_keyword('Input text', AppForm_locators.email_field, AppForm_locators.app_user_email)
        bi.run_keyword('Input text', AppForm_locators.address_field, AppForm_locators.app_user_address)
        bi.run_keyword('Input text', AppForm_locators.inst_name_field, AppForm_locators.app_user_inst_name)
        bi.run_keyword('Input text', AppForm_locators.flwrs_field, AppForm_locators.app_user_flwrs)
        bi.run_keyword('Click element', AppForm_locators.hear_about_checkbox)
        bi.run_keyword('Click element', AppForm_locators.agree_checkbox)
        bi.run_keyword('Click element', AppForm_locators.question_checkbox)
        bi.run_keyword('Input text', AppForm_locators.brief_field, AppForm_locators.brief_text)
        bi.run_keyword('Click button', AppForm_locators.app_submit_btn)
        bi.run_keyword('Wait until page contains element', AppForm_locators.challenge_message)

    # 18. Check user can submit "Ambassador application form" with incorrect data
    def submit_ambassador_appform_inc(self):
        bi.run_keyword('ambassador_app_form')
        bi.run_keyword('Input text', AppForm_locators.name_field, AppForm_locators.app_user_inc_name)
        bi.run_keyword('Input text', AppForm_locators.email_field, AppForm_locators.app_user_inc_email)
        bi.run_keyword('Input text', AppForm_locators.address_field, AppForm_locators.app_user_inc_address)
        bi.run_keyword('Input text', AppForm_locators.inst_name_field, AppForm_locators.app_user_inc_inst_name)
        bi.run_keyword('Input text', AppForm_locators.flwrs_field, AppForm_locators.app_user_inc_flwrs)
        bi.run_keyword('Click element', AppForm_locators.hear_about_checkbox)
        bi.run_keyword('Click element', AppForm_locators.agree_checkbox)
        bi.run_keyword('Click element', AppForm_locators.question_checkbox)
        bi.run_keyword('Input text', AppForm_locators.brief_field, AppForm_locators.brief_text)
        bi.run_keyword('Click button', AppForm_locators.app_submit_btn)
        bi.run_keyword('Wait until page contains element', AppForm_locators.challenge_message)
