class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Get the minimum number of bananas needed per hour / lower bound of binary search
        left = ceil(sum(piles) / h) 

        # Get the maximum number of bananas needed per hour / higher bound of binary search
        right = max(piles) 

        # While left pointer is less than or equal to right pointer we have not exhausted the possible numbers
        while left < right:
            # Get the mid point of the two pointers and test if this number of bananas per hour will finish all piles within time limit
            mid = (left + right) // 2 

            # Check if the number of banana is enough to eat per hour and finish all the piles of banana.
            total_time = 0
            for i in piles:
                total_time += ceil(i / mid)
                if total_time > h:
                    break

            # If we can finish the piles of banana, then lets try to reduce the number of banana per hour, move right pointer to mid point. The answer must be midpoint and above.
            if total_time <= h:
                right = mid 
            # If we cannot finish the piles of banana, then lets try to increase the number of bananas per hour, move left pointer to mid point. The answer cannot be left of midpoint.
            else:
                left = mid + 1

        # Return the minimum number of bananas per hour.
        return right