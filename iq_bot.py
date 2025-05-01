from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import cv2
import pytesseract

def login_and_capture():
    # Configura o Chrome para usar o perfil padrão
    chrome_options = Options()
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--start-maximized")

    # Abre a sala de negociação
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://iqoption.com/traderoom")

    # Espera a página carregar e tira o print
    time.sleep(8)
    driver.save_screenshot("static/screenshot.png")
    print("📸 Print tirado com sucesso.")

    # Lê o saldo da imagem
    imagem = cv2.imread("static/screenshot.png")
    texto = pytesseract.image_to_string(imagem, lang="eng")
    print("💰 Texto extraído:", texto)

    # Mostra o nome da URL da página
    url_atual = driver.current_url
    print(f"📂 Página aberta: {url_atual}")

    driver.quit()
    return "static/screenshot.png"

