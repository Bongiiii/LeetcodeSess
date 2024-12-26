class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        inplace addition, moving from right to left, considering the carry value along the way
        """
        n = len(digits)
        
        # Start from the rightmost digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:  # If the current digit is not 9, increment and return
                digits[i] += 1
                return digits
            else:  # If the current digit is 9, set it to 0
                digits[i] = 0
        
        # If all digits were 9, we need to add a new leading 1
        return [1] + digits