from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import zipfile
import os

# Caminho para o ChromeDriver

chrome_driver_path = r'C:\\Users\\joaov\\OneDrive\\Área de Trabalho\\chromedriver-win64\\chromedriver.exe' # Atualize para o caminho correto

# Configuração do Selenium
chrome_options = Options()

# Use o Service para passar o caminho do ChromeDriver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Acessa o site
url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
driver.get(url)

# Espera até que o link do Anexo I esteja presente
link_anexo_i = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'Anexo_I_Rol')]"))
)

# Agora você pode acessar o atributo 'href' do link
pdf_url_i = link_anexo_i.get_attribute('href')

# Encontrar o link do Anexo II
link_anexo_ii = driver.find_element(By.XPATH, "//a[contains(@href, 'Anexo_II')]")
pdf_url_ii = link_anexo_ii.get_attribute('href')

# Função para baixar os PDFs
def download_pdf(pdf_url, pdf_name):
    pdf_response = requests.get(pdf_url)
    with open(pdf_name, 'wb') as f:
        f.write(pdf_response.content)

# Baixar o PDF do Anexo I
pdf_name_i = pdf_url_i.split('/')[-1]  # Extrai o nome do arquivo a partir da URL
download_pdf(pdf_url_i, pdf_name_i)

# Baixar o PDF do Anexo II
pdf_name_ii = pdf_url_ii.split('/')[-1]  # Extrai o nome do arquivo a partir da URL
download_pdf(pdf_url_ii, pdf_name_ii)

# Compactar os arquivos PDF

zip_filename = "Anexos.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(pdf_name_i)
    zipf.write(pdf_name_ii)

# Limpar os arquivos PDF após a compactação (opcional)
os.remove(pdf_name_i)
os.remove(pdf_name_ii)

# Fechar o navegador
driver.quit()

print(f"Arquivos PDF foram baixados e compactados em {zip_filename}.")
