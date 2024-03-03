stack=[]
def push():
    data = input("Enter element")
    stack.append(data)

def pop():
    if not stack:
        print("Empty Stack")

    else:
        d=stack.pop()
        print("Element removed :" , d)


def peek():

    if not stack:
        print("Empty Stack")
    else:
      print(stack[-1])

def display():

    if(not stack):
        print("Stack is empty")
    else:
        for element in stack:
            print(element)
    

print("Select operation\n 1.push\n 2.pop\n 3.peek\n 4.display \n 5.quit\n")

while True:
    choice=int(input("Enter your choice"))
    if choice==1:
        push()
    
    elif choice==2:
        pop()

    elif choice==3:
        peek()

    elif choice==4:
        display()
        

    elif choice==5:
        break

    else:
        print("Enter the correct operation..")

        
