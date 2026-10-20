def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr


scores = [72, 88, 53, 94, 78, 60]

print("Original Exam Scores:", scores)
print("Sorted by Insertion Sort:", insertion_sort(scores))
print("Sorted by Selection Sort:", selection_sort(scores))
