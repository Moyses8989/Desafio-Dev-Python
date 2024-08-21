# Funções de teste com pytest
from arvore import Node, inserir, search, remover, inorder

def test_inserir():
    arvore = Node(50)
    arvore = inserir(arvore, 30)
    assert search(arvore, 30) is not None, "Elemento 30 não foi inserido corretamente"

def test_remover():
    arvore = Node(50)
    arvore = inserir(arvore, 30)
    arvore = remover(arvore, 30)
    assert search(arvore, 30) is None, "Elemento 30 não foi removido corretamente"

def test_inoder(capfd):
    a = Node("A")
    a = inserir(a, "B")
    a = inserir(a, "C")
    a = inserir(a, "D")
    a = inserir(a, "E")
    a = inserir(a, "J")
    inorder(a)
    out, err = capfd.readouterr()
    assert out == "A B C D E J "