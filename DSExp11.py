def linear_search(products, key):
    for i, product in enumerate(products):
        if product["id"] == key:
            return i, product
    return -1, None


def binary_search(products, key):
    low = 0
    high = len(products) - 1

    while low <= high:
        mid = (low + high) // 2

        if products[mid]["id"] == key:
            return mid, products[mid]
        elif products[mid]["id"] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, None


products = [
    {"id": 101, "name": "Laptop"},
    {"id": 202, "name": "Mobile"},
    {"id": 303, "name": "Tablet"},
    {"id": 404, "name": "Headphones"},
    {"id": 505, "name": "Keyboard"}
]

i, product = linear_search(products, 303)
print("Linear Search Result:")
print(f"Product found at index {i}: {product}")

i, product = binary_search(products, 404)
print("Binary Search Result:")
print(f"Product found at index {i}: {product}")
