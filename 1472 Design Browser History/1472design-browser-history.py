class BrowserHistory:

    def __init__(self, homepage: str):
        self.history_stack = []
        self.future_stack = []
        self.visit(homepage)

    def visit(self, url: str) -> None:
        #visiting an entirely new url clears the future stack
        self.history_stack.append(url)
        self.future_stack.clear()

    def back(self, steps: int) -> str:
        #go back and leave atleast one url in history stack
        while (steps > 0) and len(self.history_stack) > 1: 
            self.future_stack.append(self.history_stack.pop())
            steps -= 1

        return self.history_stack[-1]

    def forward(self, steps: int) -> str:
        while (steps > 0) and self.future_stack:
            self.history_stack.append(self.future_stack.pop())
            steps -= 1

        return self.history_stack[-1]
        """
        t/c :
        __init__(homepage): O(1)
        visit(url): O(1)
        back(steps): O(min(steps, len(history_stack) - 1))
        forward(steps): O(min(steps, len(future__stack)))

        s/c :
        O(n) - n being the number of urls
        """

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)