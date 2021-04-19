from robot.libraries.BuiltIn import BuiltIn
from NavPanel import NavPanel_locators
from SearchField import SearchField_locators

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class Cart_Locators:
    # ----------------- Items -------------------- #
    earrings_item_1 = 'css = a[href="/collections/earrings/products/feuille-dor-earring"]'
    necklace_item_1 = 'css = a[href="/collections/necklace/products/elephant-charm-necklace"]'
    necklace_item_2 = 'css = a[href="/collections/all/products/colgante-de-cabeza-de-flecha"]'
    rings_item_1 = 'css = a[href="/collections/rings/products/set-e"]'
    # item links
    rings_img_link = 'css = a[href="/collections/rings"]'
    # ------------------ Buttons ----------------- #
    add_to_cart_btn = 'css = #AddToCart-product-template'
    continue_btn = 'css = a.btn.btn--secondary.cart__continue.small--hide.cart__submit-control'
    right_btn = 'css = a.btn.btn--tertiary.btn--narrow'
    remove_btn = 'css = p.small--hide a.btn.btn--small.btn--tertiary.cart__remove'
    update_btn = 'css = input.btn.btn--secondary.small--hide.cart__submit-control'
    # ---------------------- Input ------------------- #
    input_block = 'css = input.cart__qty-input'
    input_field = 'css = td.text-right.small--hide input.cart__qty-input'
    # ------------------ Adding result --------------- #
    # single
    add_result = 'css = a[href="/products/feuille-dor-earring?variant=21484165857362"]'
    # several
    add_result_1 = 'css = a[href="/products/colgante-de-cabeza-de-flecha?variant=29250690220114"]'
    add_result_2 = 'css = a[href="/products/elephant-charm-necklace?variant=21484216451154"]'
    # --------------- Price value data ------------ #
    price_block = 'css = tr.cart__row.border-bottom.line1.border-top > td.cart__price-wrapper > span'
    price_value = '$28.99'
    total_price_block = 'css = tr.cart__row.border-bottom.line1.border-top > td:nth-child(5) > div > span'
    total_price_value = '$57.98'
    total_price_value_1 = '$28.99'
    # ------------------ Remove result ------------ #
    remove_result = 'Your cart is currently empty.'
    # ------------------ Search result ------------ # for TC - #11
    search_result = 'css = a.full-width-link'


class CartFunctionality(NavPanel_locators, SearchField_locators):
    # 8. Check user can add item to cart
    def add_item_to_cart(self):
        bi.run_keyword('Click element', NavPanel_locators.earrings_btn)
        bi.run_keyword('Click link', Cart_Locators.earrings_item_1)
        bi.run_keyword('Click button', Cart_Locators.add_to_cart_btn)
        bi.run_keyword('Wait until page contains element', Cart_Locators.add_result)

    # 9. Check user can delete item from cart
    def delete_item_from_cart(self):
        bi.run_keyword('Click element', NavPanel_locators.earrings_btn)
        bi.run_keyword('Click link', Cart_Locators.earrings_item_1)
        bi.run_keyword('Click button', Cart_Locators.add_to_cart_btn)
        bi.run_keyword('Click element', Cart_Locators.remove_btn)
        bi.run_keyword('Wait until page contains', Cart_Locators.remove_result)

    # 10. Check user can add several items to cart
    def add_several_items(self):
        bi.run_keyword('Click element', NavPanel_locators.necklace_btn)
        bi.run_keyword('Click link', Cart_Locators.necklace_item_1)
        bi.run_keyword('Click button', Cart_Locators.add_to_cart_btn)
        bi.run_keyword('Click link', Cart_Locators.continue_btn)
        bi.run_keyword('Click link', Cart_Locators.right_btn)
        bi.run_keyword('Click link', Cart_Locators.necklace_item_2)
        bi.run_keyword('Click button', Cart_Locators.add_to_cart_btn)
        bi.run_keyword('Wait until page contains element', Cart_Locators.add_result_1)
        bi.run_keyword('Wait until page contains element', Cart_Locators.add_result_2)

    # 11. Check user can append items in the cart
    def append_item_in_the_cart(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click link', Cart_Locators.rings_img_link)
        bi.run_keyword('Click link', Cart_Locators.rings_item_1)
        bi.run_keyword('Click button', Cart_Locators.add_to_cart_btn)
        bi.run_keyword('Element text should be', Cart_Locators.price_block, Cart_Locators.price_value)
        bi.run_keyword('Press keys', Cart_Locators.input_block, 'UP')
        bi.run_keyword('Click element', Cart_Locators.update_btn)
        bi.run_keyword('Textfield value should be', Cart_Locators.input_field, '2')
        bi.run_keyword('Element text should be', Cart_Locators.total_price_block,
                       Cart_Locators.total_price_value)

    # 12. Check user can subtract items in the cart
    def subtract_item_in_the_cart(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click link', Cart_Locators.rings_img_link)
        bi.run_keyword('Click link', Cart_Locators.rings_item_1)
        bi.run_keyword('Click button', Cart_Locators.add_to_cart_btn)
        bi.run_keyword('Press keys', Cart_Locators.input_block, 'UP')
        bi.run_keyword('Click element', Cart_Locators.update_btn)
        bi.run_keyword('Press keys', Cart_Locators.input_block, 'DOWN')
        bi.run_keyword('Click element', Cart_Locators.update_btn)
        bi.run_keyword('Textfield value should be', Cart_Locators.input_field, '1')
        bi.run_keyword('Element text should be', Cart_Locators.total_price_block,
                       Cart_Locators.total_price_value_1)

    # 13. Check system show a warning message is user subtract items in cart to ZERO
    def subtract_to_zero(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click element', SearchField_locators.magnifier_icon)
        bi.run_keyword('Input text', SearchField_locators.search_field, 'Timo Ciervo Ring')
        bi.run_keyword('Click button', SearchField_locators.search_submit_btn)
        bi.run_keyword('Click element', Cart_Locators.search_result)
        bi.run_keyword('Click button', Cart_Locators.add_to_cart_btn)
        bi.run_keyword('Press keys', Cart_Locators.input_block, 'DOWN')
        bi.run_keyword('Textfield value should be', Cart_Locators.input_field, '0')
        bi.run_keyword('Click element', Cart_Locators.update_btn)
        sl.wait_until_page_contains('Your cart is currently empty.')
