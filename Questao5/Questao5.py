import pytest

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search(root, key):
    if root is None or root.key == key:
        return root
    
    if root.key < key:
        return search(root.right, key)
    
    return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

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

# Funções de teste com pytest

def test_inserir():
    arvore = Node(50)
    arvore = inserir(arvore, 30)
    assert search(arvore, 30) is not None, "Elemento 30 não foi inserido corretamente"

def test_remover():
    arvore = Node(50)
    arvore = inserir(arvore, 30)
    arvore = remover(arvore, 30)
    assert search(arvore, 30) is None, "Elemento 30 não foi removido corretamente"