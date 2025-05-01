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
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://login.iqoption.com/pt/login")

    try:
        wait = WebDriverWait(driver, 20)

        # Fecha o aviso de cookies se aparecer
        try:
            entendi_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Entendi')]")))
            entendi_btn.click()
        except Exception:
            print("Aviso de cookies não encontrado ou já fechado.")

        # Faz login
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
