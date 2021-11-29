import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.make_sure_item_is_added_to_basket()
    page.make_sure_price_is_correct()
    # breakpoint()

#     pytest.param("bugged_link", marks=pytest.mark.xfail)

