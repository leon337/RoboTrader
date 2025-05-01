load_dotenv()
from dotenv import load_dotenv
import os
email = os.getenv("IQ_EMAIL")
senha = os.getenv("IQ_PASSWORD")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_capture():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Ative depois de testar

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://login.iqoption.com/pt/login")

    wait = WebDriverWait(driver, 20)

    try:
        # Clica no botão 'Entendi'
        entendi = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            '[data-test-id="notification-action-label"]'
        )))
        entendi.click()
        print("✅ Botão 'Entendi' clicado com sucesso.")
    except Exception:
        print("⚠️ Botão 'Entendi' não encontrado ou já removido.")

    try:
        # Fecha o aviso 'Disclaimer'
        fechar_disclaimer = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'div[class*="disclaimer"] svg use[href="#icon_general_close_thin"]'
        )))
        driver.execute_script("arguments[0].parentElement.click();", fechar_disclaimer)
        print("✅ Aviso 'Disclaimer' fechado com sucesso.")
    except Exception:
        print("⚠️ Ícone de fechar o aviso 'Disclaimer' não encontrado.")

    try:
        # Clica no campo de login e preenche
        login_input = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
        login_input.click()
        login_input.send_keys(email)

        # Clica no campo de senha e preenche
        senha_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        senha_input.click()
        senha_input.send_keys("Emilly31@72q")

        # Clica no botão Entrar
        senha_input.send_keys(Keys.RETURN)
        print("✅ Login e senha enviados.")
    except Exception:
        print("❌ Falha ao preencher ou enviar login.")
        driver.quit()
        return "static/screenshot.png"

    # Espera carregar a tela da conta
    time.sleep(7)

    # Tira print da tela
    driver.save_screenshot("static/screenshot.png")
    print("📸 Print tirado com sucesso.")

    # Captura a URL (nome do arquivo aberto)
    url_atual = driver.current_url
    print(f"📂 Nome do arquivo/página aberta: {url_atual}")

    driver.quit()
    return "static/screenshot.png"
