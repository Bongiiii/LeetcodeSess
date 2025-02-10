class MinStack:
    """
    Stack of tuples with O(1) time for all opeta
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        """
        Inorder to do the operations in O(1), be storing the min element as you append
        """
        if not self.stack:
            minElem = val

        else:
            minElem = min(val, self.stack[-1][1])

        self.stack.append((val, minElem))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()