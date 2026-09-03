class Node:
    def __init__(self,url):
        self.url = url
        self.next = None
top = None
def push(url):
    global top
    n = Node(url)
    n.next = top
    top = n

def pop():
    global top
    if top is None:
        return None
    x = top.url
    top = top.next
    return x

push("microsoftedge.com")
push("gemini.com")
push("skillrack.com")

print("Last visited (popped):",pop())
print("Last visited (popped):",pop())

class Job:
    def __init__(self,doc):
        self.doc = doc
        self.next = None
front = rear = None

def enqueue(doc):
    global front,rear
    n = Job(doc)
    if rear is None:
        front = rear = n
    else:
        rear.next = n
        rear = n

def dequeue():
    global front,rear
    if front is None:
        return None
    x = front.doc
    front = front.next
    if front is None:
        rear = None
        return x

enqueue("Document1.pdf")
enqueue("Document2.pdf")
enqueue("Document3.pdf")

print("Printing Jobs : ")
while front:
    print("Printed : ",dequeue())
