import scrapy
import json
import time
import os

class CompraAgoraSpider(scrapy.Spider):
    name = "produtos"
    login_url = "https://www.compra-agora.com/cliente/logar"
    start_urls = ["https://www.compra-agora.com/"] # Ponto de partida para a navegação
    username = "04.502.445/0001-20"
    password = "85243140"

    def __init__(self, *args, **kwargs):
        super(CompraAgoraSpider, self).__init__(*args, **kwargs)
        self.items = []  # Inicializa uma lista para armazenar os produtos

    def start_requests(self):
        # Continue to parse categories
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse_categories
        )


    def parse_categories(self, response):
        categories  = [{"id":1458, "nome": "destaques"},
                        {"id":800, "nome": "alimentos"},
                        {"id":344, "nome": "bazar"},
                        {"id":778, "nome": "bebidas"},
                        {"id":183, "nome": "bomboniere"},
                        {"id":1321, "nome": "carnes-e-congelados"},
                        {"id":180, "nome": "cuidados-pessoais"},
                        {"id":771, "nome": "laticinios"},
                        {"id":1399, "nome": "naturais-e-nutricao"},
                        {"id":926, "nome": "papelaria"},
                        {"id":215, "nome": "pet"},
                        {"id":179, "nome": "roupa-e-casa"},
                        {"id":258, "nome": "sorvetes"}]
        
        for category in categories:
            category_code = f"{category['nome']}/{category['id']}"
            api_url = f"https://www.compra-agora.com/api/catalogproducts/{category_code}"
            self.logger.info(f"Visitando a categoria: {category['nome']} - URL: {api_url}")

            yield scrapy.Request(
                url=api_url,
                callback=self.parse_products,
                meta={'category_name': category["nome"]}
            )

    def parse_products(self, response):
        items_aux = []
        products = response.json().get("produtos", [])
        for product in products:
            item = {
                "descrição": product.get("Nome"),
                "descricao_fabricante": product.get("Variacoes")[0].get("DescricaoFabricante"),
                "imagem_url": f"https://images-unilever.ifcshop.com.br/produto/{product.get('Foto')}"
            }
            items_aux.append(item) # Adiciona o item à lista de produtos
        self.logger.info(items_aux)
        self.items.extend(items_aux)  
        time.sleep(10)

    def close(self):
        output_dir = '/app/output'
        path = 'produtos.json'
        if os.path.exists(output_dir):
            path = os.path.join(output_dir, path)
        # Salvando os resultados em um arquivo JSON
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)