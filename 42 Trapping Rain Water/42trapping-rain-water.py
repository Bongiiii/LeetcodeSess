class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Understand:
        input - array, output - integer
        problem summary: given an array of heights, return the total rain water that can be trapped

        Match:
        two pointer
        array manipulation

        Plan:
        1. Use two pointers, one starting from the left (index 0) and one from the right (index len(height) - 1).
        2. Track the maximum height encountered from both sides: left_max and right_max.
        3. Move the pointers inward, calculating trapped water based on the minimum of left_max and right_max.
        4. Add the water trapped to the result until the pointers meet.
        """
        if not height:
            return 0
        
        # Initialize pointers and maximums
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        trapped_water = 0
        
        # Two-pointer approach
        while left < right:
            if height[left] <= height[right]:
                # Calculate water trapped at left
                if height[left] < left_max:
                    trapped_water += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                # Calculate water trapped at right
                if height[right] < right_max:
                    trapped_water += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        
        return trapped_water
