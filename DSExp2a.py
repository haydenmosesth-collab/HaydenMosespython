class Node:
    def __init__(self, name, phone):
        self.name, self.phone = name, phone
        self.next = None

head = None

def insert(name, phone):
    global head
    n = Node(name, phone)
    if head is None:
        head = n
    else:
        p = head
        while p.next:
            p = p.next
        p.next = n

def delete(name):
    global head
    if head and head.name == name:
        head = head.next
        return
    p = head
    while p and p.next:
        if p.next.name == name:
            p.next = p.next.next
            return
        p = p.next

def display():
    p = head
    while p:
        print(p.name, ":", p.phone)
        p = p.next

insert("Alice", "12345")
insert("Bob", "67890")
insert("Charlie", "54321")

display()
delete("Bob")
print("After deletion:")
display()
