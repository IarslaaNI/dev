from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
print("Script başladı.")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()


product_url = 'https://www.amazon.com.tr/Apple-iPhone-15-128-GB/dp/B0CHXCGHRK/ref=sr_1_1_sspa?__mk_tr_TR=ÅMÅŽÕÑ&dib=eyJ2IjoiMSJ9.9Eb4CgznipjQIqeRHEXWK5_fU8s1GZ371ljt4x_3Peta-ehpnapYQrud-BrbFnftAYObpuJ3MPd13GvO8ZHRnT_ea4W_vDawfhohOOm-nRuK_sHKGdeZqstS8vMQWJzOSOxIEeDoZL_XDJiKRdyRiH6_dUiF6r2PJYrCHoki5XwRZrFEiTws575Lit4GatrVq7o6ZMtrNBdkRSX2tB-ka_Lu8hdZisYYJv0y0CW7tc-LovcBhkeYHr4SKYWHIr5fQd9AfkXqRlaXhSusoWowA5JGhTnZ0RGVUuAfqmtI1-o.m02F4_6D0AF3ibS6698XeFw8ej3uI9XcBMTPgV20xws&dib_tag=se&keywords=Apple+iPhone+14+%28128+GB%29+-+Mavi&qid=1719772476&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
driver.get(product_url)


time.sleep(2)  
try:
    accept_cookies_button = driver.find_element(By.ID, 'sp-cc-accept')
    accept_cookies_button.click()
    print("Çerezler kabul edildi.")
except Exception as e:
    print("Çerezleri kabul et butonu bulunamadı veya zaten kabul edilmiş olabilir.")
    print(e)


time.sleep(2)


try:
    quantity_dropdown_label = driver.find_element(By.CLASS_NAME, 'a-dropdown-label')
    quantity_dropdown_label.click()
    time.sleep(1)  
    

    quantity_option = driver.find_element(By.XPATH, '//a[@id="quantity_1" and @data-value=\'{"stringVal":"2"}\']')
    quantity_option.click()
    print("Ürün adedi 2 olarak seçildi.")
except Exception as e:
    print("Ürün adedi seçilemedi.")
    print(e)

time.sleep(2)


try:
    add_to_cart_button = driver.find_element(By.ID, 'add-to-cart-button')
    add_to_cart_button.click()
    print("Ürün sepete eklendi.")
except Exception as e:
    print("Ürün sepete eklenemedi.")
    print(e)


time.sleep(2)


try:
    cart_button = driver.find_element(By.ID, 'nav-cart-count-container')
    cart_button.click()
    print("Sepete gidildi.")
except Exception as e:
    print("Sepete gidilemedi.")
    print(e)

time.sleep(2)
try:
    save_for_later_button = driver.find_element(By.CSS_SELECTOR, 'input[data-action="save-for-later"]')
    save_for_later_button.click()
    print("Daha sonrası için kaydet butonuna tıklandı.")
except Exception as e:
    print("Daha sonrası için kaydet butonuna tıklanamadı.")
    print(e)

time.sleep(20)


driver.quit()