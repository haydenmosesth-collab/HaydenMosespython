
# Minimum Cost Cable Network using Kruskal's Algorithm

cities = [
    "Chennai", "Madurai", "Trichy",
    "Salem", "Coimbatore", "Tirunelveli"
]

edges = [
    ("Chennai", "Madurai", 46),
    ("Chennai", "Trichy", 33),
    ("Chennai", "Salem", 34),
    ("Trichy", "Madurai", 13),
    ("Trichy", "Salem", 14),
    ("Salem", "Coimbatore", 16),
    ("Coimbatore", "Madurai", 21),
    ("Coimbatore", "Tirunelveli", 30),
    ("Madurai", "Tirunelveli", 15)
]

parent = {city: city for city in cities}

def find(city):
    if parent[city] != city:
        parent[city] = find(parent[city])
    return parent[city]

def union(city1, city2):
    root1 = find(city1)
    root2 = find(city2)

    if root1 != root2:
        parent[root2] = root1
        return True
    return False

edges.sort(key=lambda edge: edge[2])

total_cost = 0
selected_edges = []

for city1, city2, cost in edges:
    if union(city1, city2):
        selected_edges.append((city1, city2, cost))
        total_cost += cost

        if len(selected_edges) == len(cities) - 1:
            break

print("Minimum Cost Cable Network")
print("--------------------------------")

for city1, city2, cost in selected_edges:
    print(f"{city1} - {city2} : {cost} lakhs")

print("--------------------------------")
print("Minimum Total Cost:", total_cost, "lakhs")
