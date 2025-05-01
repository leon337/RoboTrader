from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_capture():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://login.iqoption.com/pt/login")

    wait = WebDriverWait(driver, 20)

    # Clica no botão "Entendi"
    try:
        entendi = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'div[data-test-id="notification-action-label"]'
        )))
        entendi.click()
        print("✅ Botão 'Entendi' clicado com sucesso.")
    except Exception as e:
        print(f"⚠️ Botão 'Entendi' não encontrado ou já removido. {e}")

    # Clica no botão de fechar o disclaimer (ícone SVG)
    try:
        close_icon = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//svg/use[@xlink:href='#icon_general_close_thin']/.."
        )))
        close_icon.click()
        print("✅ Botão de fechar o disclaimer clicado com sucesso.")
    except Exception as e:
        print(f"⚠️ Botão de fechar o disclaimer não encontrado. {e}")

    # Clica no link "Disclaimer completo"
    try:
        disclaimer = wait.until(EC.element_to_be_clickable((
            By.LINK_TEXT, "Disclaimer completo"
        )))
        disclaimer.click()
        print("✅ Link 'Disclaimer completo' clicado.")
        time.sleep(3)
        driver.back()  # volta para a tela de login
    except Exception as e:
        print(f"⚠️ Link 'Disclaimer completo' não encontrado. {e}")

    try:
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        email_input.send_keys("leonpcsn@gmail.com")
        password_input.send_keys("Emilly31@72@")
        password_input.send_keys(Keys.RETURN)

        time.sleep(10)
        driver.save_screenshot("static/screenshot.png")

    finally:
        driver.quit()

    return "static/screenshot.png"
