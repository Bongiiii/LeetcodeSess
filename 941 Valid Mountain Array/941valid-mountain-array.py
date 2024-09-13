class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Understand:
        input: array of integers, output: boolean
        problem summary: given a list of integers, determine if the list is a mountain or not. 
        A mountain has a length >=3, values before the peak are less than the peak and after 
        the peak are also smaller. 

        Match:
        array
        two pointer

        Clarifying questions:
        sorting is a no go as it will destroy the mountain if there
        can peak be at the first index or last index?

        Plan:
        Check Length: The array must have at least 3 elements.
        Traverse Up: Start from index 0 and move up while arr[i] < arr[i+1].
        Check Peak: After finishing the upward traversal, the peak should 
        not be the first or last element.
        Traverse Down: Continue moving down while arr[i] > arr[i+1].
        Return: If you've traversed the entire array, it’s a valid mountain array.
        
        R/E:
        s/c = O(1), t/c = O(N)
        """
         # Array must have at least 3 elements to be a valid mountain
        if len(arr) < 3:
            return False
        
        i = 0
        n = len(arr)
        
        # Traverse up: strictly increasing
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        
        # Peak can't be the first or last element
        if i == 0 or i == n - 1:
            return False
        
        # Traverse down: strictly decreasing
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        # If we reach the end of the array, it is a valid mountain
        return i == n - 1
