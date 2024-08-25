class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Understand:
        input- array nums with 3 colors 0,1,2(unsorted), output - array nums with colors sorted 0,1,2(same colors next to each other)
        do not use the sort function
        sort them in place, so no extra space...algorithm should have s/c= O(1)
        empty array is not possible as 1<=nums.length<=300
        no edge case of an other number, possible elements of nums 0,1,2

        Match:
        binary search
        loop/conditional statements
        two pointers
        dutch national flag algorithm

        Plan:
        three pointers starting on opposite sides of nums, and the scanner(dutch national flag algorithm)
        left keeps track of 0, scanner is for scanning(single scan) and right is for 2
        check if scanner is 0, if so it swaps with left and then left updates(shift 1 point up) and so does scanner
        if scanner == 1, just update scanner by 1, 
        lastly check if scanner is 2, if so swap scanner element with element on the right
        update right pointers
        """
        if len(nums) == 1:
            return nums

        left, scanner, right = 0, 0, len(nums) - 1

        while (scanner <= right):
            if nums[scanner] == 0:
                nums[scanner], nums[left] = nums[left], nums[scanner]
                left += 1
                scanner += 1

            elif nums[scanner] == 1:
                scanner += 1
            else: #nums[right] == 2
                nums[right], nums[scanner] = nums[scanner], nums[right]
                right -= 1

       