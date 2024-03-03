class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    
    def addFirst(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        newnode.next = self.head
        self.head = newnode
    
    def addlast(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newnode
        newnode.next = None
    
    def addBefore(self, data, idx):
        newnode = Node(data)
        i = 0
        temp = self.head
        while i < idx - 1:
            temp = temp.next
            i += 1
        newnode.next = temp.next
        temp.next = newnode
    
    def addAfterValue(self, data, idx):
        newnode = Node(data)
        i = 0
        temp = self.head
        while i < idx:
            temp = temp.next
            i += 1
        newnode.next = temp.next
        temp.next = newnode
    
    def DeleteFirst(self):
        if self.head == None:
            print("Empty LL")
            return
        self.head = self.head.next
    
    def deleteLast(self):
        if self.head == None:
            print("Empty LL")
            return
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
    
    def size(self):
        temp = self.head
        c = 0
        while temp != None:
            c += 1
            temp = temp.next
        return c
    
    def print(self):
        if self.head == None:
            print("Empty LL")
            return
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

l = LL()

print("1.Insert at first : ")
print("2.Insert at last : ")
print("3.Insert after a value: ")
print("4.Insert before a value : ")
print("5.Delete First: ")
print("6.Delete Last: ")
print("7.Size of LL: ")
print("8.Display")

while True:
    print("Enter choice")
    choice = int(input())
    if choice == 1:
        print("Enter data :")
        data = int(input())
        l.addFirst(data)
    elif choice == 2:
        print("Enter data :")
        data = int(input())
        l.addlast(data)
    elif choice == 3:
        print("Enter data :")
        data = int(input())
        print("Enter index before which value is to be entered")
        idx = int(input())
        l.addBefore(data, idx)
    elif choice == 4:
        print("Enter data :")
        data = int(input())
        print("Enter index after which value is to be entered")
        idx = int(input())
        l.addAfterValue(data, idx)
    elif choice == 5:
        l.DeleteFirst()
    elif choice == 6:
        l.deleteLast()
    elif choice == 7:
        print(l.size())
    elif choice == 8:
        l.print()
    else:
        break

