from collection import deque

q = deque()
n = int(input("Enter number of vehicles:"))

for i in range(n):
    q.append(input())

x = int(input("Enter number of minutes:"))

for i in range(x):
    if q:
        q.popleft()

print("Remaining Vehicles:")
for v in q:
    print(v)
