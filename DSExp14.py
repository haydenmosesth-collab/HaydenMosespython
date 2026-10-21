def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


sizes = [45, 12, 78, 23, 56, 10, 89, 33]

print("Original Item Sizes (in cm):")
print(sizes)

print("Sorted Item Sizes (in cm):")
print(quick_sort(sizes))
