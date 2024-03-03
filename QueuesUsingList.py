queue=[]
def enqueue():
    data=input("Enter data: ")
    queue.append(data)

def dequeue():
    if not queue:
        print("Queue is empty")

    else:
        p=queue.pop(0)
        print(p,"is poped")

def display():
    if not queue:
        print("Queue is empty")
    for i in queue:
        print(i)


print("Select operation\n 1.enqueue\n 2.dequeue\n 3.display \n 4.quit\n")

while True:
    choice=int(input("Enter your choice"))
    if choice==1:
        enqueue()
    
    elif choice==2:
        dequeue()

    elif choice==3:
        display()        

    elif choice==4:
        break

    else:
        print("Enter the correct operation..")