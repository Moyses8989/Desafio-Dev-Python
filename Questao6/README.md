# Projeto Questao6 com Docker

# Scraper de Citações
Este projeto contém um scraper para extrair citações de um autor específico do site Quotes to Scrape. O scraper utiliza a biblioteca Selenium para automação de navegador e a biblioteca JSON para imprimir os dados extraídos na tela.

# Visão Geral
O script realiza as seguintes etapas:

* Inicia um driver do navegador usando o Selenium.
* Navega para a página principal do site de citações.
* Extrai citações do autor especificado e suas informações biográficas.
* Navega pelas páginas para obter todas as citações disponíveis do autor.
* Imprime os dados extraídos na tela.

# Tecnologias

* Python: Linguagem de programação usada para o script.
* Selenium: Biblioteca para automação de navegador.
* JSON: Formato para imprimir os dados extraídos.

## Pré-requisitos

- **Docker**: Certifique-se de que o Docker esteja instalado na sua máquina.
- **Make (Opcional)**: Para facilitar a execução dos comandos, o `make` pode ser usado. Ele vem pré-instalado em sistemas Linux e macOS, mas pode ser instalado no Windows via [Chocolatey](https://chocolatey.org/install) ou [WSL](https://docs.microsoft.com/pt-br/windows/wsl/install).


## Estrutura do Projeto
```plaintext
questao6/
├──autor.py
├── Dockerfile
├── Makefile
├── README.md
└── requirements.txt
```


## Usando o Makefile
O `Makefile` automatiza a construção, execução e limpeza do ambiente Docker. Siga os passos abaixo para usar os comandos do `make`.

1. Construir a Imagem Docker
Para construir a imagem Docker do projeto, use:

```bash
make build
```

2. Executar o scrap de citações
Para executar o scraper dentro do container Docker basta executar:

```bash
make run python autor.py
```

3. Recompilar e Executar
Se você quiser limpar o ambiente, reconstruir a imagem Docker e executar o scraper, use:

```bash
make rebuild
```

4. Limpar o Ambiente
Para limpar o diretório de saída e remover as imagens Docker criadas:

```bash
make clean
```

## Usando Docker Diretamente
Se preferir, você também pode usar comandos Docker diretamente, sem o Makefile.

1. Construir a Imagem Docker

```bash
docker build -t questao_6 .
```

2. Executar o scrap de citações
Para executar o scraper dentro do container Docker basta executar::

```bash
docker run -it --name questao6_temp questao6 python autor.py
docker rm questao6_temp
```

3. Limpar o Ambiente
Para limpar o ambiente, remova o container temporário e a imagem Docker:

```bash
docker rmi questao6
docker system prune -f
```
