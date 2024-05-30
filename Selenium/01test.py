from selenium import webdriver # 'WEBDRIVER: módulo fornece uma interface para controlar navegadores da web. 
# Usamos isso para iniciar um navegador e realizar ações nele.
from selenium.webdriver.common.by import By 
# By: Uma classe que fornece métodos para localizar elementos na página web, 
# como By.ID, By.NAME, By.XPATH, etc.
from selenium.webdriver.common.keys import Keys
# Keys: Contém teclas especiais que podem ser usadas para simular pressionamentos de teclas, 
# como Enter, Esc, Tab, etc.
from selenium.webdriver.support.ui import WebDriverWait
# WebDriverWait: Uma classe que permite implementar esperas explícitas.
# Usada para esperar que certos elementos ou condições sejam atendidos antes de prosseguir.
from selenium.webdriver.support import expected_conditions as EC
# Um módulo que fornece condições pré-definidas que podem ser usadas com WebDriverWait.'
import time
# Módulo padrão do Python que fornece várias funções relacionadas ao tempo. 
# Aqui, usamos para pausas (sleep).
import pyautogui
# Biblioteca que permite automatizar interações com a interface gráfica do usuário, 
# como mover o mouse, clicar, digitar e tirar capturas de tela.

# Caminho para o ChromeDriver 
caminho_driver = r'C:\Users\xhenr\Desktop\Ciência de dados\Selenium\chromedriver-win64'

# Inicializa as opções do Chrome
options = webdriver.ChromeOptions()

try:

    # Inicializa o WebDriver para o Chrome. O executable_path especifica o caminho para o ChromeDriver.
        driver = webdriver.ChromeOptions(executable_path=caminho_driver, options=options)

    # Navegar para a pagina google -  não é necessário
        driver.get('https://www.google.com')

    # Encontrar o campo de busca e realizar uma pesquisa
        # Encontra o campo de busca do Google pelo nome do elemento (name='q')
        caixa_de_busca = driver.find_element(By.NAME, 'q')
        # Digita "Selenium Python" no campo de busca.
        caixa_de_busca.send_keys('Selenium Python')
        # Simula o pressionamento da tecla Enter para realizar a busca.
        caixa_de_busca.send_keys(Keys.RETURN)
        # Cria uma espera explícita de até 10 segundos.
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
        )
        # Especifica a condição de espera: a presença do elemento com ID='search', 
        # que indica que os resultados da pesquisa foram carregados.

        # Pausar para Garantir que a Página Esteja Carregada
        time.sleep(2)

finally:
    # Mantenha o navegador aberto para inspeção
    pass
