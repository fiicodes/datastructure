class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1

    def push(self,value):
        self.top+=1
        self.stack.append(value)
    def pop(self):
        if self.top==-1:
            print("Item cannot be deleted ,stack is empty!!")
        else:
            self.top-=1
            self.stack.pop()
        
    def stack_print(self):
        for i in range(self.top,-1,-1):
            if i==self.top:
                print(self.stack[i],"top")
            else:
                print(self.stack[i],"item")
                print("|")

    def peek(self):
        print(self.stack[self.top])
    


s=Stack()
s.push(5)
s.push(6)
s.push(9)
s.push(26)
s.stack_print()
s.peek()
s.pop()
s.stack_print()


     



