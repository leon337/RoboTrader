from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
import cv2
import time

def login_and_capture():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://iqoption.com/traderoom")
    time.sleep(8)
    driver.save_screenshot("static/screenshot.png")

    print("📸 Print tirado com sucesso.")

    # Leitura do saldo com OCR
    img = cv2.imread("static/screenshot.png")
    text = pytesseract.image_to_string(img, lang="eng")

    print("💰 Texto detectado na imagem:")
    print(text)

    driver.quit()
    return "static/screenshot.png"

if __name__ == '__main__':
    login_and_capture()
