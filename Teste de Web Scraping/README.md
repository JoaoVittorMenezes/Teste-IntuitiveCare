# README - Desafio 1: Web Scraping
# README - Desafio 1: Web Scraping ANS

📋 **Descrição do Projeto**  
Script Python que automatiza o download dos Anexos I e II do Rol de Procedimentos da Agência Nacional de Saúde Suplementar (ANS) e os compacta em um arquivo ZIP.

🎯 **Objetivo**  
- Acessar o site da ANS  
- Localizar e baixar os Anexos I e II em PDF  
- Compactar os arquivos em um único ZIP  
- Limpar os arquivos temporários

🛠️ **Tecnologias Utilizadas**  
- Python 3.x  
- Selenium WebDriver  
- ChromeDriver  
- Bibliotecas: requests, zipfile, os

⚙️ **Pré-requisitos**  
Antes de executar o script, você precisará:

Ter instalado:  
- Python 3.8+  
- Google Chrome  
- ChromeDriver compatível com sua versão do Chrome  

Instalar as dependências:  
 
-bash:  pip install selenium requests 

📁 **Estrutura de Arquivos**

/Teste de Web Scraping
  ├── scraping.py    # Script principal
  ├── README.md              # Este arquivo

🚀 **Como Executar**

Baixe o ChromeDriver compatível com sua versão do Chrome: https://chromedriver.chromium.org/downloads

Atualize o caminho do ChromeDriver no script:

-bash:   chrome_driver_path = r'CAMINHO_PARA_O_CHROMEDRIVER'

Execute o script:

-bash:   python scraping.py

📌 **Saída Esperada** 

Arquivo Anexos.zip contendo os PDFs baixados.

Mensagem no terminal:

-bash:  Arquivos PDF foram baixados e compactados em Anexos.zip.

⚠️ **Observações Importantes**

Certifique-se de ter:

Conexão com a internet

Permissões de escrita no diretório de execução

O script:

Pode levar alguns minutos para executar

Fecha automaticamente a janela do navegador ao finalizar

Remove os arquivos PDF após a compactação

Em caso de erro:

Verifique se o ChromeDriver está na versão correta

Confira se os links no site da ANS não foram alterados
