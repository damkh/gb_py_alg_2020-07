"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""
from collections import deque
from collections import namedtuple

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

# g = [
#     [0, 2, 0, 0, 0],
#     [3, 0, 5, 9, 0],
#     [0, 6, 0, 2, 4],
#     [0, 0, 0, 0, 1],
#     [0, 0, 3, 0, 0]
# ]


def dks(graph, start):
    start0 = start
    g_len = len(graph)
    is_visited = [False] * g_len
    cost = [float('inf')] * g_len
    parent = [-1] * g_len
    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True
        for i, ver in enumerate(g[start]):
            if ver != 0 and not is_visited[i]:
                if cost[i] > ver + cost[start]:
                    cost[i] = ver + cost[start]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(g_len):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    # print(parent)
    cost_ways = []
    cost_way = namedtuple('cost_way', 'vertex, cost, way')
    for finish in range(g_len):
        if finish != start0:
            if cost[finish] != float('inf'):
                way = deque([finish])
                i = finish
                while parent[i] != start0:
                    way.appendleft(parent[i])
                    i = parent[i]
                way.appendleft(start0)
                cost_ways.append(cost_way(finish, cost[finish], list(way)))
            else:
                cost_ways.append(cost_way(finish, cost[finish], start0))
    return cost_ways


s = int(input("Номер стартовой вершины: "))
for vertex in dks(g, s):
    if vertex.cost != float('inf'):
        print(f'Кратчайший путь от вершины {vertex.way[0]} до вершины {vertex.vertex} '
              f'по маршруту {vertex.way} стоит {vertex.cost}')
    else:
        print(f'Кратчайший путь от вершины {vertex.way} до вершины {vertex.vertex} не определен')
