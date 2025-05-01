from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import cv2
import pytesseract

def login_and_capture():
    # Configurar o Chrome para usar o perfil padrão (com login salvo)
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=/home/$USER/.config/google-chrome")
    chrome_options.add_argument("--profile-directory=Default")

    # Abrir o navegador
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://iqoption.com/traderoom")
    
    # Esperar a página carregar
    time.sleep(8)

    # Tirar o print da tela
    screenshot_path = "static/screenshot.png"
    driver.save_screenshot(screenshot_path)
    print("📸 Print tirado com sucesso.")

    # Ler a imagem e extrair o texto (OCR)
    imagem = cv2.imread(screenshot_path)
    texto_extraido = pytesseract.image_to_string(imagem, lang='eng')
    print("💰 Texto extraído do print:\n", texto_extraido)

    # Capturar URL da página aberta
    url_atual = driver.current_url
    print(f"📄 Nome do arquivo/página aberta: {url_atual}")

    driver.quit()
    return screenshot_path
