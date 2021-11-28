from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from config import PRODUCT, EMAIL, PHONE, PRICE


options = Options()
options.headless = True
browser = webdriver.Chrome(
    executable_path="/home/imtoopunkforyou/prog/kekez/chromedriver", options=options)


if __name__ == "__main__":
    start_time = time.time()
    try:
        browser.get('https://www.donationalerts.com/r/samual')
        time.sleep(1)
        # DONATOR NAME
        print("Ввожу данные в поле Donator_name \n")
        donator_name_input = browser.find_element(By.ID, 'donatorName')
        donator_name_input.clear()
        donator_name_input.send_keys(PRODUCT)
        time.sleep(1)
        # MESSAGE
        print("Ввожу данные в поле Message \n")
        message_input = browser.find_element(
            By.XPATH, '//div[@id="editable-area"]')
        message_input.clear()
        message_input.send_keys(EMAIL)
        time.sleep(1)
        # AMOUNT
        print("Ввожу данные в поле Amount \n")
        amount_input = browser.find_element(By.XPATH, '//input[@id="amount"]')
        amount_input.clear()
        amount_input.send_keys(PRICE)
        time.sleep(1)
        # SUBMIT
        submit_input = browser.find_element(
            By.CLASS_NAME, 'da-ga.b-btn._fill._round-anim.s-round-anim._send-donation')
        submit_input.click()
        time.sleep(3)
        # PAYMENT METHOD
        print("Выбираю способ оплаты \n")
        qiwi_btn = browser.find_element(
            By.CSS_SELECTOR, 'div.da-ga.s-pay-group-primary.b-pay__system-item.s-pay-system-item.billing-method-container.billing-method-container-QIWI_MYCOM.billing-method.billing-method-QIWI_MYCOM')
        qiwi_btn.click()
        time.sleep(1)
        # EMAIL IN DONATIONALERTS
        print("Ввожу данные в поле Email \n")
        email_input_da = browser.find_element(By.NAME, 'email')
        email_input_da.clear()
        email_input_da.send_keys(EMAIL)
        time.sleep(1)
        # QIWI WALLET
        print("Ввожу данные в поле Phone_number \n")
        qiwi_wallet = browser.find_element(By.NAME, 'phone_number')
        qiwi_wallet.clear()
        qiwi_wallet.send_keys(PHONE)
        time.sleep(1)
        # FINISH BTN
        print("Готовлю ссылку  \n")
        finish_btn = browser.find_element(
            By.CSS_SELECTOR, 'div.b-btn._fill._round-anim.s-round-anim')
        finish_btn.click()
        time.sleep(20)
        url = browser.current_url
        filename = f'{PRODUCT}_{PHONE}_{PRICE}.txt'
        with open(filename, 'w', newline='') as file:
            file.write(url)
    except Exception:
        print(Exception)
    finally:
        browser.close()
        browser.quit()
        print("РАБОТА ОКОНЧЕНА \n")
        print("Создан файл " + filename + "\n")
        print("Прошло времени: %s секунд" %
              str(int((time.time() - start_time))))
