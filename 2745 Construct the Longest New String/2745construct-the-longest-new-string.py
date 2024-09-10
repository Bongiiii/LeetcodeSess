class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        a = min(x, y)
        
        if x == y:
            return 2 * (x + y + z)
        elif x == a:
            return 2 * (x + x + 1 + z)
        else:
            return 2 * (y + 1 + y + z)