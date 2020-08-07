"""
3. Написать программу, которая обходит невзвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random
from collections import deque
from collections import namedtuple


def gen_graph(n):
    return [[random.randint(0, 1) if i != j else 0 for i in range(n)] for j in range(n)]


def dfs():
    start = stack.pop(-1)
    if start == 'end':
        return
    # print(f'- start: {start}')
    is_visited[start] = True
    # print(f'-- is_visited: {is_visited}')

    for i, ver in enumerate(g[start]):
        # print(f'-- i: {i}')
        # print(f'-- cost: {cost}')
        if ver != 0:
            if cost[i] > ver + cost[start]:
                cost[i] = ver + cost[start]
                parent[i] = start
                # print(f'--- parent: {parent}')
                # print(f'--- cost: {cost}')
                if not is_visited[i]:
                    stack.append(i)
                    # print(f'--- start: {start}')
                    dfs()
    # print(f'-! start: {start}')


# g = [
#     [0, 1, 1, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0, 0, 1, 0],
#     [0, 0, 0, 1, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 1, 1, 0],
# ]

num = int(input("Введите количество вершин: "))
while True:
    s = int(input("Номер стартовой вершины: "))
    if 0 <= s < num:
        break
    else:
        print('Номер стартовой вершины должен быть в диапазоне [0; num), где num - количество вершин')
g = gen_graph(num)
print('Граф в виде матрицы смежности:')
[[print(g[i][j], end=' ') if j < num - 1 else print(g[i][j]) for j in range(num)] for i in range(num)]

g_len = len(g)
is_visited = [False] * g_len
parent = [-1] * g_len
cost = [float('inf')] * g_len
cost[s] = 0
stack = ['end', s]
dfs()
# print(f'parent: {parent}')
ways = []
way_nt = namedtuple('way', 'vertex, way')
for finish in range(g_len):
    if parent[finish] != -1:
        if finish != s:
            way = deque([finish])
            i = finish
            while parent[i] != s:
                way.appendleft(parent[i])
                i = parent[i]
            way.appendleft(s)
            ways.append(way_nt(finish, list(way)))
        else:
            ways.append(way_nt(finish, s))
    else:
        ways.append(way_nt(finish, 0))

for vertex in ways:
    if vertex.vertex != s:
        if vertex.way != 0:
            print(f'Путь от вершины {vertex.way[0]} до вершины {vertex.vertex}: {vertex.way}')
        else:
            print(f'Путь от вершины {s} до вершины {vertex.vertex} не определен')
