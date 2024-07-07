class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #stack to keep track of log operations
        stack = []

        #iteratively go through the log operations
        for log in logs:
            if log == "../":
                # stack is not empty
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)
        return len(stack)
