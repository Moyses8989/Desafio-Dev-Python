# Imagem base
FROM python:3.6-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do projeto para o diretório de trabalho
COPY arvore.py ./
COPY /tests/. ./tests/
COPY pyproject.toml ./

# Defina o comando padrão para rodar o spider
ENTRYPOINT ["pytest", "."]