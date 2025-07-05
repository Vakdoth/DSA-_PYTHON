class node:
    def  __init__[self,data=none,next=none]:
    
    self.data= data 
    self.next=next_node
    
class linked:
    def __inti__(self):
        self.head = none 
        
    def insert (self,data):
        node = node(data)
        node.next = self.head
        self.head = node
        
    def display(self):
        if self.head is none:
            print("np data")
            
        else:
            n= self.head
            while n is not none:
                print (n.data,end='')
                print("__",end= '')
                
                n=n.next 
        print('none')
        
ll=lnked()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()