"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from binarytree import bst


def search(bin_search_tree, number, path=''):
    if bin_search_tree.value == number:
        return f'Число {number} обнаружено по следующему пути:\nКорень {path}'
    if number < bin_search_tree.value and bin_search_tree.left != None:
        pass



bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Введите число для поиска: '))
print(search(bt, num))

