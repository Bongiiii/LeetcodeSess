class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Understand:
        input - array of integers, integer and output - array of booleans

        Match:
        array manipulation

        Plan:
        do in place array update to optimize space
        firstly find the current max in the candies array
        then that integer will be used to compare and update the resultant array
        if the kid at that index after giving extra candy has the max or more
         than max candy update the element to truth else false
        once you have updated all elements break out of the loop and return the initial array

        R/E:
        s/c = O(1)
        t/c = O(N)
        """
        maximum = max(candies)  # Find the current maximum number of candies.
        # Use a list comprehension to compute the result:
        return [candy + extraCandies >= maximum for candy in candies]