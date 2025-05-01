from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_capture():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Descomente para rodar em segundo plano
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://login.iqoption.com/pt/login")

    wait = WebDriverWait(driver, 20)

    # Primeiro tenta clicar com XPath
    try:
        entendi_xpath = '//button[contains(text(), "Entendi")]'
        entendi_btn = wait.until(EC.element_to_be_clickable((By.XPATH, entendi_xpath)))
        entendi_btn.click()
        print("✅ Botão 'Entendi' clicado com sucesso (via XPath).")
    except:
        # Se não conseguir, tenta por texto dentro de todos os botões
        try:
            print("⚠️ XPath falhou. Tentando localizar botão por texto...")
            botoes = driver.find_elements(By.TAG_NAME, "button")
            for btn in botoes:
                if "Entendi" in btn.text:
                    driver.execute_script("arguments[0].click();", btn)
                    print("✅ Botão 'Entendi' clicado com sucesso (via texto).")
                    break
            else:
                print("⚠️ Nenhum botão com texto 'Entendi' encontrado.")
        except Exception as e:
            print(f"❌ Erro ao procurar botão por texto: {e}")

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
