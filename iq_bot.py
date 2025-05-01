from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_capture():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Ative se quiser ocultar o navegador
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://iqoption.com/traderoom")

    time.sleep(7)

    # Tirar print da tela
    driver.save_screenshot("static/screenshot.png")
    print("📸 Print tirado com sucesso.")

    # Captura a URL atual
    url_atual = driver.current_url
    print(f"📂 Nome do arquivo/página aberta: {url_atual}")

    driver.quit()
    return "static/screenshot.png"

