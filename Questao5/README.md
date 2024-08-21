# Projeto Questao5 com Docker

# Criação de uma estrutura de dados Arvore binária.

# Estrutura do projeto

```plaintext
questao5/
├── Dockerfile
├── README.md
├── requirements.txt
└── arvore.py

```

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

O teste unitário irá validar se um elemento foi devidamente inserido na arvore e também validará a remoção de um elemento. O teste pode ser aplicado de duas formas.

* Através de validação com If e else.

'''python
def realizar_teste_unitario(elemento_testado, funcao_teste, parametros_extras_funcao_teste, funcao_validacao_resultado):
    resultado = funcao_teste(elemento_testado, parametros_extras_funcao_teste)
    validacao, mensagem_de_erro = funcao_validacao_resultado(elemento_testado, parametros_extras_funcao_teste)

    if validacao:
        print(f"Teste da função {funcao_teste.__name__}: Sucesso!")
    else:
        print(f"Teste da função {funcao_teste.__name__}: Erro! Mensagem de Erro: {mensagem_de_erro}")

def validar_insercao(arvore, valor_inserido):
    if search(arvore, valor_inserido):
        return True, None
    else:
        return False, f"Elemento {valor_inserido} não encontrado"

def validar_remocao(arvore, valor_removido):
    if search(arvore, valor_removido):
        return False, f"Elemento {valor_removido} encontrado"
    else:
        return True, None

arvore = Node(50)
realizar_teste_unitario(arvore, inserir, 30, validar_insercao)
realizar_teste_unitario(arvore, remover, 30, validar_remocao)

'''

* Ou então, utilizando a bliblioteca `pytest`. O  `pytest` é uma biblioteca própria para a realização de testes unitários em python, sendo um método muito prático. A instrução `passert` fará a validação da condição aplicada. Se o resultado for verdadeiro, o script continuará sua execução, mas se o resultado for falso, o retorno será um `AssertionError`.

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

## Usando Docker

1. Construir a Imagem Docker

```bash
docker build -t questao_5 .
```

2. Executar o Container
Execute o container com o comando docker run <nome_da_imagem>

```bash
docker run -d --name questao5_temp questao_5
```

3. Limpar o Ambiente
Para limpar o ambiente, remova o container temporário e a imagem Docker:

```bash
docker rmi questao2
docker system prune -f
```

