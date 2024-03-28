class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Single_LL:
    def __init__(self):
        self.head=None
    def insert_element(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while  temp.next!=None:
                temp=temp.next
            temp.next=new_node
    def insert_begin(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def delete_Lnode(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            prev=self.head
            while temp.next!=None:
                prev=temp
                temp=temp.next
            prev.next=None
    def delete_value(self,value):
        prev=None
        temp=self.head
        if temp.data==value:
            self.head=self.head.next
            return True
        while temp.data!=value and temp.next!=None:
            prev=temp
            temp=temp.next
        if temp.data==value:
            prev.next=temp.next
            return True
        else:
            return False
    def search(self,element):
        temp=self.head
        while temp.data!=element and temp.next!=None:
            temp=temp.next
        if temp.data==element:
            print("Element Found")
            return temp
        else:
            return False
    def update(self,old,new):
        s=self.search(old)
        if s:
            s.data=new
        else:
            print("Not found data")
            
            
            
    def print_element(self):
        temp=self.head
        while temp.next!=None:
            print(temp.data)
            temp=temp.next
        print(temp.data)

        
SLL=Single_LL()
while True:
    print("1. Insert element 2.insert begin 3. delete Lasst node 4.delete value 5.print List 6.search 7.update  ")
    ch=int(input("Enter your choice : "))
    if ch==1:
        element=int(input("Enter the element : "))
        SLL.insert_element(element)
    elif ch==2:
        element=int(input("Enter the element : "))
        SLL.insert_begin(element)
    elif ch==3:
        SLL.delete_Lnode()
    elif ch==4:
        element=int(input("Enter the element to delete : "))
        print(SLL.delete_value(element))
    elif ch==5:
        SLL.print_element()
    elif ch==6:
        element=int(input("Enter the element : "))
        SLL.search(element)
    elif ch==7:
        old,new=map(int,input().split())
        SLL.update(old,new)
    else:
        break
        
