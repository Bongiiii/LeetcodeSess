class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        Understand:
        input - array of integers, output - array of integers
        Prob summary: given an array of height of people in a queue, return an array, with the number of people each
        person can see to their right

        Match:
        array
        two pointers

        Plan:
        solve using the input array
        use two pointers, pointer to count the number of people each person can see to their right
        and the second pointer will be marking the person who we are counting the people to their right
        when you have traversed the whole array return the original array

        R/E:
        s/c = O(1), use of variables and inplace edits
        t/c = O(N) 
        """
        # Result array to store the number of people each person can see to their right
        result = [0] * len(heights)
        stack = []

        # Traverse from right to left
        for i in range(len(heights) - 1, -1, -1):
            visible_count = 0
            # Pop all shorter people from the stack, they are visible to heights[i]
            while stack and stack[-1] < heights[i]:
                stack.pop()
                visible_count += 1
            
            # If there's someone taller or equal to heights[i], they block the view further right
            if stack:
                visible_count += 1
            
            # Store the count of visible people for heights[i]
            result[i] = visible_count
            # Push current height onto the stack
            stack.append(heights[i])

        return result