class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Understand:
        Input: An array of integers nums where nums contains n+1 integers. Each integer is between
         1 and n (inclusive), meaning at least one number is repeated.
        Output: The number that appears more than once (duplicate).
        Constraint: Solve the problem without modifying the array and using only constant extra 
         space (O(1) space complexity).

        Match:
        Algorithm: Use Floyd's Tortoise and Hare algorithm, which is commonly used to detect cycles in linked lists.
        Why this algorithm: The problem can be treated as cycle detection. Each element in the array
         points to an index (similar to how nodes in a linked list point to the next node). 
         Since there is a duplicate number, this creates a cycle.
        
        Plan:
        Treat the array as a linked list:

        Each element in the array can be considered as pointing to another index. For any element nums[i], it "points" 
         to nums[nums[i]], just like a node in a linked list points to the next node.
        Due to the presence of a duplicate, there is a cycle in this "linked list."
        Detect the cycle using Floyd's Tortoise and Hare Algorithm:

        Initialize two pointers, slow and fast, both starting at nums[0].
        Move slow by 1 step (slow = nums[slow]) and fast by 2 steps (fast = nums[nums[fast]]) through the array.
        If there is a cycle, these two pointers will eventually meet at some point inside the cycle.
        Find the start of the cycle (duplicate):

        After the pointers meet, reset one of the pointers (slow) to the start of the array (slow = nums[0]).
        Move both pointers (slow and fast) one step at a time (slow = nums[slow], fast = nums[fast]) until they meet again.
        The point where they meet is the starting point of the cycle, which corresponds to the duplicate number.
        Key Point on Memory Addresses:
        Array as Linked List: In this problem, we don't deal with actual memory addresses, but we treat the indices
         and values in the array as if they were "addresses" and "pointers" respectively:
        nums[i] is the "pointer" at index i, and the value nums[i] is the next "address" (or index) that it points to.
        Essentially, nums[i] acts like a pointer to the next element (just like in a linked list), and traversing 
        the array using nums[nums[i]] mimics following pointers in a linked list.
        
        R/E:
        s/c = O(1)
        t/c = O(N)

        """
        # Phase 1: Detect the cycle (duplicate)
        slow = nums[0]
        fast = nums[0]
        
        # Move slow by 1 step and fast by 2 steps
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:  # Cycle detected
                break
        
        # Phase 2: Find the start of the cycle (duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow  # The duplicate number