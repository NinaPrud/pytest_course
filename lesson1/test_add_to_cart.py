from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_item_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    #time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()
    #time.sleep(3)

    remove_button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="remove-sauce-labs-backpack"]')
    print(remove_button.text)
    assert remove_button.text == 'Remove'

    text_item_for_cart = driver.find_element(By.CSS_SELECTOR, 'a#item_4_title_link > div.inventory_item_name').text

    cart_btn = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
    cart_btn.click()
   # time.sleep(3)
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'

    text_item_in_cart = driver.find_element(By.CSS_SELECTOR, 'a#item_4_title_link > div.inventory_item_name').text
    print(f'\n{text_item_in_cart} = {text_item_for_cart}')
    assert text_item_in_cart == text_item_for_cart

    driver.quit()
