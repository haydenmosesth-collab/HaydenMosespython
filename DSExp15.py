class HashTable:
    def __init__(self, size):
        self.size = size
        self.linear = [None] * size
        self.quadratic = [None] * size

    def insert_linear(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.linear[pos] is None:
                self.linear[pos] = key
                return

    def insert_quadratic(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.quadratic[pos] is None:
                self.quadratic[pos] = key
                return

    def display(self, table, title):
        print(title)

        for i in range(self.size):
            print(f"Index {i}: {table[i]}")


ht = HashTable(7)
keys = [10, 20, 5, 15, 7]

for key in keys:
    ht.insert_linear(key)
    ht.insert_quadratic(key)

ht.display(ht.linear, "Hash Table (Linear Probing):")
ht.display(ht.quadratic, "Hash Table (Quadratic Probing):")
