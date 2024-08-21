import scrapy
import json

class CompraAgoraSpider(scrapy.Spider):
    name = "produtos"
    login_url = "https://www.compra-agora.com/cliente/logar"
    start_urls = ["https://www.compra-agora.com/"] # Ponto de partida para a navegação
    username = "04.502.445/0001-20"
    password = "85243140"

    def __init__(self, *args, **kwargs):
        super(CompraAgoraSpider, self).__init__(*args, **kwargs)
        self.items = []  # Inicializa uma lista para armazenar os produtos

    # def start_requests(self):
    #     # Hash the password using pynacl (Blake2b with a key as an example)
    #     hashed_password = blake2b(self.password.encode(), key=b'secret_key', encoder=HexEncoder)

    #     # Fazendo login
    #     yield FormRequest(
    #         url=self.login_url,
    #         method="POST",
    #         formdata={"login": self.username, "senha": hashed_password.decode()},
    #         callback=self.after_login
    #     )

    def start_requests(self):
        # Verifica se o login foi bem-sucedido
        # if "minha-conta" in response.url:
        self.log("Login bem-sucedido.")
        # Continue to parse categories
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse_categories
        )
        # else:
        #     self.log("Falha no login.")


    def parse_categories(self, response):
        categories = categories = [{"id":1458, "nome": "destaques"},
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
            self.log(f"Visitando a categoria: {category['nome']} - URL: {api_url}")

            yield scrapy.Request(
                url=api_url,
                callback=self.parse_products,
                meta={'category_name': category["nome"]}
            )

    def parse_products(self, response):
        category_name = response.meta['category_name']
        products = response.json().get("produtos", [])
        for product in products:
            item = {
                "Categoria": category_name,
                "Descrição": product.get("Nome"),
                "Fabricante": product.get("Fabricante"),
                "URL": product.get("Url")
            }
            self.items.append(item)  # Adiciona o item à lista de produtos

    def close(self, reason):
        # Salvando os resultados em um arquivo JSON
        with open('produtos.json', 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)