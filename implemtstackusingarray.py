class MyStack:
    def __init__(self):
        self.arr = []

    # Function to push an integer into the stack.
    def push(self, data):
        self.arr.append(data)

    # Function to remove an item from the top of the stack.
    def pop(self):
        if not self.arr:
            return -1  # Return -1 if the stack is empty
        return self.arr.pop()  # Return the top element after popping