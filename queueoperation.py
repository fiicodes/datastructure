from collections import deque
class Queue:
    def __init__(self):
        self.queue=deque()
       
    

    def insert(self,value):
        self.queue.append(value)

    

    
    def delete(self):
        if len(self.queue)>0:
          self.queue.pop()
        return None
    

    def __str__(self):
       return str(self.queue)
    

my_q=Queue()
my_q.insert(100)
my_q.insert(200)
my_q.insert(300)
print(my_q)
my_q.delete()
print(my_q)


   


        
