from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def extrair_citacoes(autor: str):
    driver.get('http://quotes.toscrape.com/')

    citacoes = []
    autor_info = {}

    try:
        while True:
            quotes = driver.find_elements(By.CLASS_NAME, 'quote')
            for quote in quotes:
                author = quote.find_element(By.CLASS_NAME, 'author').text
                if author == autor_nome:
                    text = quote.find_element(By.CLASS_NAME, 'text').text
                    tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, 'tag')]
                    citacoes.append({'text': text, 'tags': tags})

                    about_button = quote.find_element(By.XPATH, './/a[contains(text(), "(about)")]')
                    about_button.click()

                    autor_info['name'] = driver.find_element(By.CLASS_NAME, 'author-title').text
                    autor_info['birthdate'] = driver.find_element(By.CLASS_NAME, 'author-born-date').text
                    autor_info['bio'] = driver.find_element(By.CLASS_NAME, 'author-description').text
                    driver.back()
                    break

            next_button = driver.find_elements(By.XPATH, '//li[@class="next"]/a')
            if next_button:
                next_button[0].click()
            else:
                break
    finally:
        driver.quit()

    return citacoes, autor_info


if __name__ == '__main__':
    autor_nome = 'J.K. Rowling'
    citacoes, autor_info = extrair_citacoes(autor_nome)

    print("\nInformações do Autor:")
    print(autor_info)

    print("Citações:")
    for citacao in citacoes:
        print(citacao)
