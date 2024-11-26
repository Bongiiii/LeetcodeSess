class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Understand:
        input - array of integers, integer and output - boolean

        Match:
        two pointer/ pointers
        array manipulation

        Plan:
        start pointer at 1, then check if that spot element is 1 or 0, if it's 1 increment pointer
        else: check if previous is (pointer - 1) is not 1 and next is not 1, then put a flower there
        and increment pointer
        once you have run out of flowers to plan, then return true else false since you can't 
        plant all flowers

        R/E:
        s/c = O(1), inplace update
        t/c = O(N)
        """
        # If no flowers need to be planted, return True
        if n == 0:
            return True

        # Iterate through the flowerbed
        for i in range(len(flowerbed)):
            # Check if the current spot is empty and its neighbors are empty or out of bounds
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                # Plant a flower
                flowerbed[i] = 1
                n -= 1  # Decrease the number of flowers left to plant
                # If all flowers are planted, return True
                if n == 0:
                    return True
        
        # If we exit the loop and still have flowers to plant, return False
        return n == 0