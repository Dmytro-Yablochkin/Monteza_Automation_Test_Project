from robot.libraries.BuiltIn import BuiltIn

bi = BuiltIn()


class NavPanel_locators:
    # Home
    home_btn = 'css = #AccessibleNav a[href="/"]'
    redirect_page = 'css = h1.collection-hero__title.page-width'

    # Earrings
    earrings_btn = 'css = #SiteNav a[href="/collections/earrings"]'
    # Bracelet
    bracelet_btn = 'css = #SiteNav a[href="/collections/bracelet"]'
    # Necklace
    necklace_btn = 'css = #SiteNav a[href="/collections/necklace"]'
    # Rings
    rings_btn = 'css = #SiteNav a[href="https://monteza.shop/collections/rings"]'
    # Partner program page
    partner_btn = 'css = #SiteNav a[href="http://partners.monteza.shop"]'
    partner_page = 'Join our partner program!'


class NavPanel:
    # 1. 2. 3. 4. 5. Check Nav-panel functionality
    def click_and_check(self):
        bi.run_keyword('Wait until page contains element', NavPanel_locators.redirect_page)
        bi.run_keyword('Click element', NavPanel_locators.home_btn)

    def nav_panel_btns(self):
        # Earrings page
        bi.run_keyword('Click element', NavPanel_locators.earrings_btn)
        bi.run_keyword('click_and_check')
        # Bracelet page
        bi.run_keyword('Click element', NavPanel_locators.bracelet_btn)
        bi.run_keyword('click_and_check')
        # Necklace page
        bi.run_keyword('Click element', NavPanel_locators.necklace_btn)
        bi.run_keyword('click_and_check')
        # Rings page
        bi.run_keyword('Click element', NavPanel_locators.rings_btn)
        bi.run_keyword('click_and_check')
        # Partner program page
        bi.run_keyword('Click element', NavPanel_locators.partner_btn)
        bi.run_keyword('Wait until page contains', NavPanel_locators.partner_page)