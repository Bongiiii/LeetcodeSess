class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [float('inf')] * n

        # First pass: left to right
        pos = -float('inf')
        
        for i in range(n):
            if s[i] == c:
                pos = i
            result[i] = min(result[i], abs(i - pos))
        
        # Second pass: right to left
        pos = float('inf')
        for i in range(n-1, -1, -1):
            if s[i] == c:
                pos = i
            result[i] = min(result[i], abs(i - pos))
        
        return result
        
        
                