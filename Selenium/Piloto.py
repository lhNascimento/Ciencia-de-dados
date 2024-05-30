from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar o WebDriver - abrir chrome
navegador = webdriver.Chrome()

# Acessa o site
navegador.get('http://127.0.0.1:5500/Selenium/04.html')

# Mapear onde estão os números da senha (1298) e clicar neles
numeros_senha = ["1", "2", "9", "8"]  # definição da senha que deve ser digitada
for numero in numeros_senha:  # percorre a lista numeros_senha, um elemento por vez, armazena esse elemento na variavel numero
    botao_numero = navegador.find_element(By.XPATH, f"//button[@valortecla='{numero}']")  # percorre as teclas onde estao os numeros, verifica se o valor da tecla bate com o valor da variavel numero
    botao_numero.click()  # após a variavel numero bater com o valor da tecla, ele clica na tecla
    time.sleep(0.5)  # Pausa para simular um clique humano
    # refaz todo esse processo até preencher a senha

# Aguardar um tempo para o login ser efetuado
time.sleep(1)

navegador.find_element(By.ID, 'login-button').click()  # clica no botao para logar

# Não fechar o navegador após fazer login (manter aberto)
while True:
    pass