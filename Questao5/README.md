# Criação de uma estrutura de dados Arvore binária.

## O que é uma árvore binária?

- Uma árvore binária é uma estrutura não linear, ou seja, apresenta múltiplos caminhos a serem percorridos. A árvore se inicia com um nó principal chamado de Raiz e a partir dessa raiz, criam-se os nós que são chamados de "filhos" e cada nó pode ter apenas 2 filhos, um criado a esqueda e o outro a direita do nó pai.

    * Nós: A parte fundamental de uma árvore binária, onde cada nó contém dados e se vincula a dois nós filhos.
    * Raiz : O nó mais alto em uma árvore é conhecido como nó raiz. Ele não tem pai e serve como ponto de partida para todos os nós na árvore.
    * Nó Pai : Um nó que tem um ou mais nós filhos. Em uma árvore binária, cada nó pode ter no máximo dois filhos.
    * Nó filho : um nó que é descendente de outro nó (seu pai).
    * Nó Folha : Um nó que não tem filhos.
    * Nó Interno : Um nó que tem pelo menos um filho. Isso inclui todos os nós, exceto os nós raiz e folha .
    Profundidade de uma Árvore Binária : O número de arestas de um nó específico até o nó raiz. A profundidade do nó raiz é zero.
    * Altura de uma árvore binária : o número de nós do nó folha mais profundo até o nó raiz.

# Criação da árvore binária

## Estrutura da Classe Node
    
* A primeira coisa a fazer é definir uma classe Node que representará cada nó da árvore binária. Cada nó conterá uma chave (key) e referências para os nós à esquerda (left) e à direita (right).

'''python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''

## Função de Busca

* A função search busca por um nó na árvore binária de busca com uma chave específica. Se o nó com a chave for encontrado, ele é retornado. Caso contrário, a função continua a busca recursivamente pela subárvore esquerda ou direita.

'''python
def search(root, key):
    if root is None or root.key == key:
        return root
    
    if root.key < key:
        return search(root.right, key)
    
    return search(root.left, key)
'''

## Percurso em Ordem (Inorder)

* A função inorder imprime os elementos da árvore binária de forma ordenada (em ordem crescente). Ela percorre a subárvore esquerda, imprime o nó atual, e depois percorre a subárvore direita.

'''python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
'''

## Função de Inserção

* A função inserir insere um novo nó na árvore binária de busca. Se a árvore estiver vazia, ela cria um novo nó. Caso contrário, ela insere o nó na subárvore esquerda ou direita com base na comparação da chave.

'''python
def inserir(root, key):
    if root is None:
        return Node(key)
    
    if root.key == key:
        return root
    
    if root.key < key:
        root.right = inserir(root.right, key)
    else:
        root.left = inserir(root.left, key)
    
    return root
'''

## Função de Remoção

* A função remover exclui um nó da árvore binária de busca. Se o nó a ser removido tiver dois filhos, a função busca o sucessor do nó (menor valor da subárvore direita), substitui a chave do nó pelo sucessor, e remove o sucessor da subárvore direita.

'''python
def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def remover(root, x):
    if root is None:
        return root

    if root.key > x:
        root.left = remover(root.left, x)
    elif root.key < x:
        root.right = remover(root.right, x)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        succ = get_successor(root)
        root.key = succ.key
        root.right = remover(root.right, succ.key)
        
    return root
'''

# Testes unitários com Pytest

* A linguagem python possuí uma biblioteca especificada para realização de testes automatizados, a lib pytest permite que um teste seja realizado de maneira simples  apenas pela identificação de "test" no nome da função. A instrução assert valida se a condição que está sendo testada é verdadeira ou falsa. Se a condição for verdadeira, a execução do script continua, contudo, se a condição for falsa, o pytest apresentará um AssertionError.

*  **Testar Inserção:** O teste cria uma árvore e insere um elemento. Depois, verifica se o elemento foi corretamente inserido usando a função search.

'''python
def test_inserir():
    arvore = Node(50)
    arvore = inserir(arvore, 30)
    assert search(arvore, 30) is not None, "Elemento 30 não foi inserido corretamente"
'''

* **Testar Remoção:** O teste cria uma árvore, insere um elemento, remove o elemento, e verifica se ele foi removido corretamente.

'''python
def test_remover():
    arvore = Node(50)
    arvore = inserir(arvore, 30)
    arvore = remover(arvore, 30)
    assert search(arvore, 30) is None, "Elemento 30 não foi removido corretamente"
'''

# Comando de execução.

Os arquivos serão executar via container docker. O arquivo dockerfile anexo utiliza a imagem do python 3.6 ou superior, define o diretorio para /app, instala o pytest, copia o arquivo .py e executa com o comando CMD ["pytest", "Questao5.py"].

Para executar o docker, primeiramente precisa-se criar a imagem de acordo com o arquivo, para isso, utiliza-se o comando: "docker build -t questao5:v1 .", A flag -t permite que você adicione uma tag para sua imagem.

![Criando a imagem](Imagens/buid_image.png)

A flag -t permite que você adicione uma tag para sua imagem.

Após buidar a imagem, podemos execurar o container docker com o comando

### Retorno no console

![Teste realizado](./Imagens/pytest.png)

