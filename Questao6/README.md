# Questão 6

O Selenium é um recurso que nunca utilizei antes para web scraping. PAra concluir essa questão, está sendo utilizado o webdriver e o By. O Webdriver simula um navegador e pode ser utilizado com o navegador a sua escolha, neste caso, estou utilizando o chrome. Já o By é utilizado para busca de elementos na página.

* A função de extrair citações será responsável pela busca e armazenamento das informações desejadas, neste caso, as citações e Tags relacionada ao autor desejado.

* O comando driver.get inicia o navegador.

* As variaveis ciratações e autor_info irão armazenar as informações coletadas do site.

* O bloco try é utilizado para gerar exceções tratar os erros internamentes.

* O laço While truta garante que enquanto houver com citações para percorrer.

* O comando "driver.find_elements(By.CLASS_NAME, 'quote')" encontra todos os elementos de citação através da classe Name.

* A condição  "if" verifica se o nome do autor na pagica corresponde ao procurado, caso sim, irá extrair as informações e tags e irá clicar no botão "about" através da função "about_button.click()", que identifica o botão pelo Xpath. Após clicar no botão abount, irá extrair as informações de nome, aniversário e bio do autor e depois fechará a nova página, retornando para a anterior, encerrando o if.

* Por fim, o script verificar se há um botão "next" para avançar para as proximas páginas, caso sim, ele irá clicar no botão até chegar a última e irá armazenando todas as citações e tags relacionadas ao autor pesquisado.

*  E para o melhor gerenciamento, cria-se uma "main" a fim de se obter uma melhor organização e controle do código.

## Resultado retornado

**Retorno obtido:**
![Retorno Autor](Questao6/Imagens/Selenium.PNG)


## Execução do script

   * **Passo 1** - Criar um docketfile
   * **Passo 2** - Criar a imagem do docket com o comando: docker build -t questao6:q6 .