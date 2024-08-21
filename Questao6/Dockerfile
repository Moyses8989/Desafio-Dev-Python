# Use uma imagem base do Python
FROM python:3.9-slim-buster

# Instale as dependências necessárias para rodar o Chrome e o Chromedriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    --no-install-recommends

# Instale o Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && apt-get install -y google-chrome-stable --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos e o script Python
COPY autor.py .
COPY requirements.txt .

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para rodar o script Python
CMD ["python", "autor.py"]
