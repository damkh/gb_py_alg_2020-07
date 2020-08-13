"""
2. Закодируйте любую строку по алгоритму Хаффмана.

Для подсчета количества символов во фразе используется collections.Counter
В качестве очереди с количеством символом используется heapq. Поэтому, фраза 'beep boop beer!',
рассмотренная преподавателем в видео, кодируется по-другому. Это связано с тем, что при вставке элемента в heapq,
элемент вставляется после равного ему элемент (между равным и бОльшим). Поэтому ветки дерева могут менять свои
направления (вместо левого - правый и наоборот).
"""
from collections import Counter
import heapq


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def expand(self, code, sym_start):
        if self.left:
            self.left.expand(code, sym_start + "0")
        if self.right:
            self.right.expand(code, sym_start + "1")
        if sym_start:
            code[self.data] = sym_start
        else:
            code[self.data] = '0'


def huff(phrase):
    # print(phrase)
    phrase_count = Counter(phrase)
    # print(phrase_count)
    hp = []
    for key, val in phrase_count.items():
        hp.append([val, len(hp), Node(data=key)])
    # print(f'hp: {hp}')
    heapq.heapify(hp)
    # print(f'heapify hp: {hp}')
    t = len(hp)
    # print(f'- t: {t}')
    while len(hp) >= 2:
        el = heapq.heappop(hp)
        count1, symbol1 = el[0], el[2]
        el = heapq.heappop(hp)
        count2, symbol2 = el[0], el[2]
        heapq.heappush(hp, [count1 + count2, t, Node(left=symbol1, right=symbol2)])
        t += 1
        # print(f'-- hp: {hp}')
    code = {}
    if hp:
        root_node = hp[0][2]
        root_node.expand(code, '')
    return code


in_phrase = input('Введите фразу: ')
codes = huff(in_phrase)
phrase_huff = ""
# if in_phrase:
for s in in_phrase:
    phrase_huff += " ".join(codes[s])
print(f'Закодированная фраза: {phrase_huff}')
print('Коды каждого символа:')
for key, val in codes.items():
    if key:
        print(f'\'{key}\': {val}')

