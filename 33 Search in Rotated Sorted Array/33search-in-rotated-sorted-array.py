class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Understand:
        input - array of integers and integer, output - integer
        edge case: can an array be rotated and have more than one pivot[6,7,4,5,0,1,2] ?

        Match:
        binary search(quick sort/ pivot sort)
        pointers(two)

        Plan:
        initialize two pointers, left and right that will start on opp ends of the array nums
        have a mid pointer that runs inside the while loop, which is valid only when left <= right
        mid is found by adding left and right and dividing by 2
        compare value at mid with target value. if value is equal to target, return target, pivot index has been found
        if less than change left to mid 
        and if greater than change right to mid
        finally return -1 if none of the conditions were satisfied

        R/E:
        s/c = O(1), t/c = O(log(n))
        """
        left, right = 0, len(nums) - 1

        while (left <= right):
            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid

            # Determine which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1