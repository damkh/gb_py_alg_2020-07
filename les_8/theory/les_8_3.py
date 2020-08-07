from _collections import deque


g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]


def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]
    # print(is_visited)

    deq = deque([start])
    print(deq)
    is_visited[start] = True
    s = '*'
    while len(deq) > 0:
        print(f'{s} deq: {deq}')
        s += '*'
        current = deq.pop()
        print(f'-- current: {current}')
        if current == finish:
            # return parent
            print(f'finish is here')
            break
        for i, vertex in enumerate(graph[current]):
            print(f'i: {i}, vertex: {vertex}')
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)
        print(f'is_visited: {is_visited}')
    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'
    print(parent)
    cost = 0
    way = deque([finish])
    i = finish
    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)
    return f'Best way from {start} to {finish} with cost: {cost} - {list(way)}'


print(bfs(g, 1, 2))
