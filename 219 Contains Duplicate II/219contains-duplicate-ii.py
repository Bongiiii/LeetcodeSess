class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tracker = {}
        for i, num in enumerate(nums):
            if num in tracker and abs((tracker[num]) - i) <= k:
                return True
                

            tracker[num] = i

        return False
