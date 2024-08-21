# Nome da imagem Docker
IMAGE_NAME = questao5

# Comando para construir a imagem Docker
build:
	docker build -t $(IMAGE_NAME) .

# Comando para executar o container Docker
run:
	docker run -it --name $(IMAGE_NAME)_temp $(IMAGE_NAME)
	docker wait $(IMAGE_NAME)_temp
	docker rm $(IMAGE_NAME)_temp

# Comando para limpar os arquivos de saída e remover imagens Docker não usadas
clean:
	docker rmi $(IMAGE_NAME)
	docker system prune -f

# Comando para reconstruir e executar
rebuild: clean build