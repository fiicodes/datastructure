# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.front=None
    def push(self,x):
        if not self.stack1:
            self.front=x
        self.stack1.append(x)
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        ans=self.stack2.pop()
        return ans
    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        return self.front

if __name__ == "__main__" :
    n = int(input())
    que = Solution()
    for _ in range(n):
        inp = input()
        command = int(inp.split(" ")[0])
        if command == 1:
            que.push(inp.split(" ")[1])
        elif command == 2:
            que.pop()
        elif command == 3:
            print(que.peek())





