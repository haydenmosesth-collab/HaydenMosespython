class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, patient, priority):
        self.heap.append((priority, patient))
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent][0] > self.heap[i][0]:
                self.heap[parent], self.heap[i] = (
                    self.heap[i], self.heap[parent]
                )
                i = parent
            else:
                break

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left

        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = (
                self.heap[smallest], self.heap[i]
            )
            self.heapify(smallest)

    def extract_min(self):
        if not self.heap:
            return None

        result = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self.heapify(0)

        return result


h = MinHeap()

patients = [
    ("Alice", 5),
    ("Bob", 3),
    ("Charlie", 1),
    ("David", 4),
    ("Eva", 2)
]

for patient, priority in patients:
    h.insert(patient, priority)

print("Current ER Queue (Priority, Patient):")
for priority, patient in sorted(h.heap):
    print(f"Priority: {priority} - Patient: {patient}")

while h.heap:
    priority, patient = h.extract_min()
    print(f"Treating: {patient} (Severity: {priority})")
