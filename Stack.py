class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,e):
        element=e
        self.stack.append(e)
        print("element is successfully pushed")
    def pop(self):
        self.stack.pop()

    def display(self):
        print(self.stack)
    def peek(self):
        print("The peek element is : ",self.stack[-1])
        
s=Stack()  
while True:
    print("1.push 2. pop 3.display 4.peek 5.exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        element=int(input("Enter the element : "))
        s.push(element)
        print("Element has been pushed")
    elif ch==2:
        s.pop()
        print("Element has been poped")
    elif ch==3:
        s.display()
    elif ch==4:
        s.peek()
    else:
        break




    

