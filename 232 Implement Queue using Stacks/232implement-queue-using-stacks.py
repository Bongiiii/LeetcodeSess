class MyQueue:
    def __init__(self):
        # Stack to handle push operations
        self.stack_in = []
        # Stack to handle pop and peek operations
        self.stack_out = []

    def push(self, x: int) -> None:
        # Push element onto stack_in
        self.stack_in.append(x)

    def pop(self) -> int:
        # Ensure stack_out has the elements in the correct order for FIFO
        if not self.stack_out:
            # Move all elements from stack_in to stack_out if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Pop from stack_out which is the front of the queue
        return self.stack_out.pop()

    def peek(self) -> int:
        # Ensure stack_out has the elements in the correct order for FIFO
        if not self.stack_out:
            # Move all elements from stack_in to stack_out if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Peek at the front element of the queue
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.stack_in and not self.stack_out
