class Node:
    """Class to represent a node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    """Class to represent the stack using linked list."""
    def __init__(self):
        self.top = None  # Initialize the stack with no elements

    def push(self, data):
        """Adds a new element to the top of the stack."""
        new_node = Node(data)  # Create a new node
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node  # Update the top pointer to the new node

    def pop(self):
        """Removes and returns the top element of the stack."""
        if self.top is None:  # Check if the stack is empty
            return -1  # Return -1 for an empty stack
        popped_data = self.top.data  # Get the data from the top node
        self.top = self.top.next  # Update the top pointer to the next node
        return popped_data
        # Add code here
