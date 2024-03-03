class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Stack:

    def __init__(self):
        self.head = None
 
    def push(self, data):
 
        if self.head == None:
            self.head = Node(data)
 
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
 
   
    def pop(self):
 
        if self.head==None:
            return None
 
        else:
            
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data
 
    def display(self):
 
        temp = self.head
        if self.head==None:
            print("Stack Underflow")
 
        else:
 
            while(temp != None):
 
                print(temp.data, end = " ")
                temp = temp.next
               
            return
 
 

s= Stack()
   
s.push(11)
s.push(22)
s.push(33)
s.push(44)
s.display()
s.pop()
print('\n')
s.display()
