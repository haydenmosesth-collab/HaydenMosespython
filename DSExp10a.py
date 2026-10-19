def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:
        return False

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

    return True


def kruskal(vertices, edges):
    parent = list(range(vertices))
    rank = [0] * vertices
    mst = []

    edges.sort(key=lambda edge: edge[2])

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))

        if len(mst) == vertices - 1:
            break

    return mst


edges = [
    (0, 1, 10),
    (1, 2, 5),
    (0, 2, 6)
]

mst = kruskal(3, edges)

print("Edges in MST:", end=" ")
print(", ".join(map(str, mst)))
