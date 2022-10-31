from selenium.webdriver.common.by import By
import time


def test_page_must_be_displayed_in_selected_language(browser, browser_language):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(15)
    browser.get(link)
    print(browser_language)
    lang_dict = {'ar': 'أضف الى سلة التسوق', 'ca': 'Afegeix a la cistella', 'cs': 'Vložit do košíku',
                 'da': 'Læg i kurv', 'de': 'In Warenkorb legen', 'en-gb': 'Add to basket', 'el': 'Προσθήκη στο καλάθι',
                 'es': 'Añadir al carrito', 'fi': 'Lisää koriin', 'fr': 'Ajouter au panier',
                 'it': 'Aggiungi al carrello', 'ko': '장바구니 담기', 'nl': 'Voeg aan winkelmand toe',
                 'pl': 'Dodaj do koszyka', 'pt': 'Adicionar ao carrinho', 'pt-br': 'Adicionar à cesta',
                 'ro': 'Adauga in cos', 'ru': 'Добавить в корзину', 'sk': 'Pridať do košíka', 'uk': 'Додати в кошик',
                 'zh-hans': 'Add to basket'}
    assert lang_dict[browser_language] in (add_to_cart_button_value := browser.find_element(By.CSS_SELECTOR,
"button.btn-add-to-basket").text), \
f'Expected to see "{lang_dict[browser_language]}", but received "{add_to_cart_button_value}"'
