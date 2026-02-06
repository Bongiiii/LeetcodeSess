class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        """brute force
        have an array to store the elements that satisfy max<=min*k...so min and max
        and then return difference in len of orig array and the new array

        optimal approach:
        since we don't care about the elements but count to be removed,
         we could use pointers, binary search and sort the array first
         sort array first
         treat every num encountered as min,
          and find count of elements that can be kept,
           any existing before them
        finally since we are tracking elements kept and qn requires min removed so 
        return len of nums - count of kept
        """
        nums.sort()
        maxKept = 0

        for i, num in enumerate(nums):
            j = bisect_right(nums, k * num)

            maxKept = max(maxKept, j - i)

        return len(nums) - maxKept
        

        