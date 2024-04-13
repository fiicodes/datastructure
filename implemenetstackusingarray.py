
class Stack:
    def __init__(self, n: int):
        self.capacity = n
        self.stack = []

    def push(self, num: int):
        if len(self.stack) < self.capacity:
            self.stack.append(num)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def isEmpty(self) -> int:
        if not self.stack:
            return 1
        else:
            return 0

    def isFull(self) -> int:
        if len(self.stack) == self.capacity:
            return 1
        else:
            return 0

