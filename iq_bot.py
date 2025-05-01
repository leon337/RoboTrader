from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_capture():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://login.iqoption.com/pt/login")

    try:
        wait = WebDriverWait(driver, 20)

        # Força clique em qualquer botão que tenha o texto "Entendi"
        try:
            botoes = driver.find_elements(By.TAG_NAME, "button")
            for btn in botoes:
                if "Entendi" in btn.text:
                    driver.execute_script("arguments[0].click();", btn)
                    print("✅ Botão 'Entendi' clicado com sucesso.")
                    break
        except Exception:
            print("⚠️ Nenhum botão com texto 'Entendi' encontrado.")

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
