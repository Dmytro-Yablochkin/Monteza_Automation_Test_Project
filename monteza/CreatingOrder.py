from robot.libraries.BuiltIn import BuiltIn
from UserData import UserData

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class Order_locators:
    contact_page = 'Contact information'

    num_email_field = 'css = #checkout_email_or_phone'
    first_name_field = 'css = input[placeholder="First name"]'
    last_name_field = 'css = input[placeholder="Last name"]'
    address_field = 'css = input[placeholder="Address"]'
    apartment_field = 'css = input[placeholder="Apartment, suite, etc. (optional)"]'
    city_field = 'css = input[placeholder="City"]'
    zip_field = 'css = input[placeholder="ZIP code"]'
    phone_number_field = 'css = input[placeholder="Phone"]'

    country_list = 'css = select.field__input.field__input--select'
    country_droplist = 'css = div.field.field--required.field--active'
    current_country = 'css = option[value="United States"]'

    flag_sign = 'css = div.section.section--contact-information > ' \
                'div.section__content > div.fieldset > div > div > div > select'
    num_country_list = 'css = div.flag-selector--focus'
    current_num_country = 'css = option[value="US"]'

    offers_checkbox = 'css = #checkout_buyer_accepts_marketing'
    save_info_btn = 'css = #checkout_remember_me'

    buy_btn = 'css = button.shopify-payment-button__button'
    cont_shipp_btn = 'css = #continue_button'

    standart_shipping = 'css = #checkout_shipping_rate_id_shopify-standard20us20shipping-23_87'
    priority_shipping = 'css = div:nth-child(3) > div'

    card_info_block = 'css = #payment-gateway-subfields-39580500050'

    # ------------------ Item order data ----------------------#
    necklace_link = 'css =  div.collection-grid-item a[href="/collections/necklace"]'
    necklace_item = 'css = a[href="/collections/necklace/products/semiluna-necklace"]'


class CreatingOrder(UserData):
    # 19. Check user can create an order with correct phone number
    def creating_an_order_via_phone_number(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click element', Order_locators.necklace_link)
        bi.run_keyword('Click link', Order_locators.necklace_item)
        bi.run_keyword('Click button', Order_locators.buy_btn)
        bi.run_keyword('Wait until page contains', Order_locators.contact_page)
        bi.run_keyword('Input text', Order_locators.num_email_field, UserData.user_phone_number)
        bi.run_keyword('Wait until page contains element', Order_locators.flag_sign)
        bi.run_keyword('Click element', Order_locators.flag_sign)
        bi.run_keyword('Wait until page contains element', Order_locators.num_country_list)
        bi.run_keyword('Click element', Order_locators.current_num_country)
        bi.run_keyword('Click element', Order_locators.offers_checkbox)
        bi.run_keyword('Input text', Order_locators.first_name_field, UserData.user_name)
        bi.run_keyword('Input text', Order_locators.last_name_field, UserData.user_last_name)
        bi.run_keyword('Input text', Order_locators.address_field, UserData.user_full_address)
        bi.run_keyword('Input text', Order_locators.apartment_field, 'Apartment')
        bi.run_keyword('Input text', Order_locators.city_field, UserData.user_city)
        bi.run_keyword('Click element', Order_locators.country_list)
        bi.run_keyword('Wait until page contains element', Order_locators.country_droplist)
        bi.run_keyword('Click element', Order_locators.current_country)
        bi.run_keyword('Input text', Order_locators.zip_field, UserData.user_zip)
        bi.run_keyword('Click element', Order_locators.save_info_btn)
        bi.run_keyword('Click button', Order_locators.cont_shipp_btn)
        bi.run_keyword('Wait until page contains', 'Shipping method')
        bi.run_keyword('Click element', Order_locators.priority_shipping)
        bi.run_keyword('Click button', Order_locators.cont_shipp_btn)
        bi.run_keyword('Wait until page contains element', Order_locators.card_info_block)

    # 20. Check user can create an order with correct email address
    def creating_an_order_via_email(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click element', Order_locators.necklace_link)
        bi.run_keyword('Click link', Order_locators.necklace_item)
        bi.run_keyword('Click button', Order_locators.buy_btn)
        bi.run_keyword('Wait until page contains', Order_locators.contact_page)
        bi.run_keyword('Input text', Order_locators.num_email_field, UserData.user_email)
        bi.run_keyword('Click element', Order_locators.offers_checkbox)
        bi.run_keyword('Input text', Order_locators.first_name_field, UserData.user_name)
        bi.run_keyword('Input text', Order_locators.last_name_field, UserData.user_last_name)
        bi.run_keyword('Input text', Order_locators.address_field, UserData.user_full_address)
        bi.run_keyword('Input text', Order_locators.apartment_field, 'Apartment')
        bi.run_keyword('Input text', Order_locators.city_field, UserData.user_city)
        bi.run_keyword('Click element', Order_locators.country_list)
        bi.run_keyword('Wait until page contains element', Order_locators.country_droplist)
        bi.run_keyword('Click element', Order_locators.current_country)
        bi.run_keyword('Input text', Order_locators.phone_number_field, UserData.user_current_number)
        bi.run_keyword('Input text', Order_locators.zip_field, UserData.user_zip)
        bi.run_keyword('Click element', Order_locators.save_info_btn)
        bi.run_keyword('Click button', Order_locators.cont_shipp_btn)
        bi.run_keyword('Wait until page contains', 'Shipping method')
        bi.run_keyword('Click element', Order_locators.standart_shipping)
        bi.run_keyword('Click button', Order_locators.cont_shipp_btn)
        bi.run_keyword('Wait until page contains element', Order_locators.card_info_block)