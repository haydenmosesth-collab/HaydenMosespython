def merge_sort(expenses):
    if len(expenses) <= 1:
        return expenses

    mid = len(expenses) // 2
    left = merge_sort(expenses[:mid])
    right = merge_sort(expenses[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


expenses = [
    ("Rent", 15000),
    ("Food", 5000),
    ("Utilities", 3000),
    ("Travel", 4500),
    ("Miscellaneous", 2500)
]

print("Original Monthly Expenses:")
for name, amount in expenses:
    print(f"{name}: ₹{amount}")

sorted_expenses = merge_sort(expenses)

print("Sorted Monthly Expenses (Ascending):")
for name, amount in sorted_expenses:
    print(f"{name}: ₹{amount}")
