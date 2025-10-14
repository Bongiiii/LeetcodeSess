class NumArray:

    def __init__(self, nums: List[int]):
        self.sumPref = [0]
        for num in nums:
            self.sumPref.append(self.sumPref[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumPref[right+1] - self.sumPref[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)