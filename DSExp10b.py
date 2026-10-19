import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start, start)]
    mst = []

    while min_heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(min_heap)

        if v in visited:
            continue

        visited.add(v)

        if u != v:
            mst.append((u, v, weight))

        for neighbor, edge_weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(
                    min_heap, (edge_weight, v, neighbor)
                )

    return mst


graph = {
    'A': [('C', 1), ('B', 2)],
    'B': [('A', 2), ('E', 1)],
    'C': [('A', 1)],
    'D': [('E', 1)],
    'E': [('B', 1), ('D', 1)]
}

mst = prim(graph, 'A')

print("Minimum Spanning Tree:")
print(mst)
