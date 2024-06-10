from collections import deque

def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Використання алгоритмів для пошуку шляху від 'A' до 'F'
start, goal = 'A', 'F'
dfs_paths = list(dfs(G, start, goal))
bfs_paths = list(bfs(G, start, goal))

print("Шляхи знайдені за допомогою DFS:", dfs_paths)
print("Шляхи знайдені за допомогою BFS:", bfs_paths)
