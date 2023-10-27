from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import os
import keyboard

# chrome_options = Options()
# chrome_options.add_argument('--headless')  # Ativa o modo headless

# # Inicializar o driver do Chrome com as opções configuradas
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
# Abrir a página de login

# Localizar e preencher o campo de nome de usuário

def login(nickname, passcode):
    driver.get('https://painel.dphsystem.com.br/login')

    username = driver.find_element(By.ID, '#select2')
    username.send_keys(nickname)

    # Localizar e preencher o campo de senha
    password = driver.find_element(By.ID, 'senha')
    password.send_keys(passcode)

    # Localizar e clicar no botão de login
    login_button = driver.find_element(By.CLASS_NAME, 'bg-primary')
    login_button.click()

def get_script(url):
    driver.get(url)

    elements = driver.find_elements() #missing
    for i in range(len(elements)):
        elements[i] = elements[i].text

# # Após o login, você pode continuar a interagir com o site como um usuário autenticado
# driver.get('https://onesystems.tech/documentos/legislacao')

# sentences = driver.find_elements(By.TAG_NAME, 'p')
# for i in range(len(sentences)):
#     sentences[i] = sentences[i].text
# print(sentences)
# # Fechar o navegador quando terminar