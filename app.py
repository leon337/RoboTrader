from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import cv2
import pytesseract
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login_and_capture():
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=/home/sophia/.config/google-chrome")
    chrome_options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://iqoption.com/traderoom")

    # Espera para a página carregar
    time.sleep(8)

    # Tira print da tela
    driver.save_screenshot("static/screenshot.png")
    print("📸 Print tirado com sucesso.")

    # Captura e processa o saldo com OCR
    imagem = cv2.imread("static/screenshot.png")
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    saldo_extraido = pytesseract.image_to_string(imagem_cinza)

    driver.quit()

    return render_template("index.html", screenshot="static/screenshot.png", saldo=saldo_extraido)

if __name__ == "__main__":
    app.run(debug=True)
