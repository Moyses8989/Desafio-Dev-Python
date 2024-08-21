import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Função para iniciar o driver do navegador
def iniciar_driver():
    return webdriver.Chrome()

# Função para abrir a página principal
def abrir_pagina_principal(driver):
    driver.get('http://quotes.toscrape.com/')

# Função para extrair citações do autor
def extrair_citacoes_do_autor(driver, autor_nome):
    citacoes = []
    while True:
        quotes = driver.find_elements(By.CLASS_NAME, 'quote')
        for quote in quotes:
            author = quote.find_element(By.CLASS_NAME, 'author').text
            if author == autor_nome:
                text = quote.find_element(By.CLASS_NAME, 'text').text
                tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, 'tag')]
                citacoes.append({'text': text, 'tags': tags})
        if not clicar_botao_proximo(driver):
            break
    return citacoes

# Função para clicar no botão "Próximo"
def clicar_botao_proximo(driver):
    next_button = driver.find_elements(By.XPATH, '//li[@class="next"]/a')
    if next_button:
        next_button[0].click()
        return True
    return False

# Função para extrair informações do autor com espera explícita
def extrair_informacoes_do_autor(driver, quote):
    autor_info = {}
    try:
        # Espera explícita para garantir que o botão "about" esteja presente
        about_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/a[contains(text(), "(about)")]'))
        )
        about_button.click()

        # Extraindo as informações do autor
        autor_info['name'] = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'author-title'))
        ).text
        autor_info['birthdate'] = driver.find_element(By.CLASS_NAME, 'author-born-date').text
        autor_info['bio'] = driver.find_element(By.CLASS_NAME, 'author-description').text

    except Exception as e:
        print(f"Erro ao extrair informações do autor: {e}")

    finally:
        driver.back()

    return autor_info

def processar_extracao(autor_nome):
    driver = iniciar_driver()
    abrir_pagina_principal(driver)

    autor_info = {}
    citacoes = []

    try:
        while True:
            quotes = driver.find_elements(By.CLASS_NAME, 'quote')
            for quote in quotes:
                author = quote.find_element(By.CLASS_NAME, 'author').text
                if author == autor_nome:
                    citacao = extrair_citacoes_do_autor(driver, autor_nome)
                    citacoes.extend(citacao)
                    autor_info = extrair_informacoes_do_autor(driver, quote)
                    break
            if not clicar_botao_proximo(driver):
                break
    finally:
        driver.quit()

    return citacoes, autor_info

# Função para salvar as informações em um arquivo JSON
def salvar_em_json(citacoes, autor_info, arquivo):
    dados = {
        'autor': autor_info,
        'citacoes': citacoes
    }

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    autor_nome = 'J.K. Rowling'
    citacoes, autor_info = processar_extracao(autor_nome)

    print("\nInformações do Autor:")
    print(autor_info)

    print("\nCitações:")
    for citacao in citacoes:
        print(citacao)
