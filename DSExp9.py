import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    pq = [(0, source)]

    while pq:
        distance, node = heapq.heappop(pq)

        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances


graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('D', 1)],
    'C': [('B', 3), ('D', 8)],
    'D': []
}

source = 'A'

print(dijkstra(graph, source))
