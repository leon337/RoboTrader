from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_capture():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://login.iqoption.com/pt/login")

    wait = WebDriverWait(driver, 20)

    # --- CLICA NO BOTÃO "ENTENDI" ---
    try:
        entendi = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'div[data-test-id="notification-action-label"]'
        )))
        entendi.click()
        print("✅ Botão 'Entendi' clicado com sucesso.")
    except Exception as e:
        print(f"⚠️ Botão 'Entendi' não encontrado ou já removido.")

    # --- CLICA NO ÍCONE DE FECHAR AVISO DO DISCLAIMER ---
    try:
        fechar_disclaimer = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'div[class*="disclaimer"] svg use[href="#icon_general_close_thin"]'
        )))
        driver.execute_script("arguments[0].parentElement.click();", fechar_disclaimer)
        print("✅ Aviso 'Disclaimer' fechado com sucesso.")
    except Exception as e:
        print("⚠️ Ícone de fechar o aviso 'Disclaimer' não encontrado.")

    # --- LOGIN ---
    try:
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        email_input.send_keys("leonpcsn@gmail.com")
        password_input.send_keys("Emilly31@72@")
        password_input.send_keys(Keys.RETURN)

        print("✅ Login enviado.")
    except Exception as e:
        print("❌ Falha ao preencher o login.")

    time.sleep(10)
    driver.save_screenshot("static/screenshot.png")

    driver.quit()
    return "static/screenshot.png"
