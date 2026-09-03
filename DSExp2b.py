n = int(input("Enter number of books : "))
books = list(map(int,input("Enter book IDs : ").split()))

stack = []
def push(x):
    stack.append(x)

def pop():
    return stack.pop()

for x in books:
    push(x)

print("Book IDs in reverse order : ",end=" ")
while stack:
    print(pop(),end=" ")
