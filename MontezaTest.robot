*** Settings ***
Documentation    Test for testing web-site functionality

Library    SeleniumLibrary
Library    monteza/NavPanel.py
Library    monteza/SearchField.py
Library    monteza/CartFunctionality.py
Library    monteza/Other&Links.py
Library    monteza/AppForm.py
Library    monteza/CreatingOrder.py

Test Setup    OPEN BROWSER   ${MAIN_PAGE_URL}    chrome
Test Teardown    Close all browsers

*** Variables ***

${MAIN_PAGE_URL}    https://monteza.shop/

*** Test Cases ***

#NAV PANEL FUNCTIONALITY
1. 2. 3. 4. 5. Check Nav-panel functionality
    [Tags]    awd
    Nav panel btns

#SEARCH FIELD FUNCTIONALITY
6. Check user can navigate to search result page with correct info in search field
    Check search field
7. "Check user can navigate to search result page with empty space in search field"
    Check search field inc

#CART FUNCTIONALITY
8. Check user can add item to cart
    Add item to cart
9. Check user can delete item from cart
    Delete item from cart
10. Check user can add several items to cart
    Add several items
11. Check user can append items in the cart
    Append item in the cart
12. Check user can subtract items in the cart
    Subtract item in the cart
13. Check system show a warning message is user substract items in cart to ZERO
    Subtract to zero

#LINKS
14. Check user can navigate to "Instagram" page
    Navigate to inst page
15. Check user can navigate to "Terms, Conditions, and Policies" page
    Navigate to terms page

#OTHER
16. Check "Youtube" video block functionality
    Youtube block

#AMBASSADOR APPLICATION FORM
17. Check user can submit "Ambassador application form" with correct data
    Submit ambassador appform
18. Check user can submit "Ambassador application form" with incorrect data
    Submit ambassador appform inc

#CREATING AN ORDER
19. Check user can create an order with correct phone number
    Creating an order via phone number
20. Check user can create an order with correct email address
    Creating an order via email