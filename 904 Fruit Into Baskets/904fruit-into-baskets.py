class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Dictionary to store the count of each type of fruit in the current window
        basket = {}
        left = 0
        max_fruits = 0

        # Iterate through the list of fruits using a sliding window
        for right in range(len(fruits)):
            # Add the current fruit to the basket
            if fruits[right] in basket:
                basket[fruits[right]] += 1
            else:
                basket[fruits[right]] = 1
            
            # If we have more than 2 types of fruits, shrink the window from the left
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            # Calculate the number of fruits in the current window and update the max
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits



