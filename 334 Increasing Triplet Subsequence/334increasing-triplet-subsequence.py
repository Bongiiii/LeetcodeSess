class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Understand:
        input - array of integers, output - boolean

        Match:
        sliding window
        two pointers

        Plan:
        base case of a single integer, return true
        traverse through the array, and check if values are increasing
        when you are using a 3 window sliding window, when you encouter a number that messes the window, update start of window

        R/E:
        s/c = O(1)
        t/c = O(N)
        """
        small = float('inf')  # Initialize to infinity
        middle = float('inf')  # Initialize to infinity

        for num in nums:
            if num <= small:
                small = num  # Update smallest number
            elif num <= middle:
                middle = num  # Update second smallest number
            else:
                # Found a number greater than both small and middle
                return True

        return False