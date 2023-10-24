from typing import List
class Solution:
    def findFirst(self,nums: List[int], target: int) -> List[int]:
        left =0
        right =len(nums)-1
        while(left<=right):
            mid = (right+left)//2
            if nums[mid]==target:
                #if this is the last occurrence of target, return mid
                if mid==0 or nums[mid-1]!=target:
                    return mid

                right = mid - 1
            elif nums[mid]>target:
                right = mid -1
            else:
                left=mid+1
        return -1

    def findLast(self,nums: List[int], target: int) -> List[int]:
        left =0
        right =len(nums)-1
        while(left<=right):
            mid = (right+left)//2
            if nums[mid]==target:
            #if this is the first occurence of target , return mid
                if mid==len(nums)-1 or nums[mid+1]!=target:
                    return mid
                left = mid + 1
            elif nums[mid]>target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1,-1]

        first = self.findFirst(nums,target)
        last = self.findLast(nums,target)

        return [first,last]

       

                

            