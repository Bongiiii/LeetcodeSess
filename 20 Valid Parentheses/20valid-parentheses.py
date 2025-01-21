class Solution:
    def isValid(self, s: str) -> bool:
        #mapping dictionary
        mapDict, stack = {"}":"{", "]":"[", ")":"("}, []

        for char in s:
            if char in "[{(":
                stack.append(char)

            elif char in "]})":
                if not stack or stack[-1] != mapDict[char]:
                    return False

                stack.pop()

        return not stack
