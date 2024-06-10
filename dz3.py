import heapq

# Додавання ваг до ребер
weighted_edges = [("A", "B", 1), ("A", "C", 2), ("B", "C", 1), ("B", "D", 4), ("C", "E", 7), ("D", "E", 2), ("D", "F", 3), ("E", "F", 1)]
G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from(weighted_edges)

def dijkstra(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, attributes in graph[current_node].items():
            distance = current_distance + attributes['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Знаходження найкоротшого шляху від 'A' до всіх інших вершин
distances = dijkstra(G_weighted, 'A')
print("Найкоротші шляхи від 'A':", distances)
