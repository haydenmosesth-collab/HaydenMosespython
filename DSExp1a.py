s = []
s.append("KA01AB1234")
s.append("KA01CD5678")
print("\n===Stack Test===")
print("Popped:",s.pop())

q=[]
q.append("KA41EF4321")
q.append("KA42GH5678")
print("\n===Queue Test===")
print("Dequeued:",q.pop(0))

size = 3
cq = [None]*size
front = rear = -1

def enqueue(x):
    global front, rear
    if (rear +1) % size == front:
        print("Overflow")
    elif front == -1:
        front = rear = 0
        cq[rear] = x
    else:
        rear = (rear + 1) % size
        cq[rear] = x

def dequeue():
    global front, rear
    if front == -1:
        print("Underflow")
    else:
        x = cq[front]
        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % size
        return x

        
enqueue("KA17HG7070")
enqueue("KA18IJ8080")
print("\n===Circular Queue Test===")
print("Dequeued:",dequeue())



        
