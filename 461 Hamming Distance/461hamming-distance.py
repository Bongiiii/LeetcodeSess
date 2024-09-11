class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Compute the XOR of x and y
        xor = x ^ y
        
        # Count the number of 1's in the binary representation of the XOR result
        distance = bin(xor).count('1')
        
        return distance
