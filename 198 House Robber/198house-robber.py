class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Understand:
        input - array, output - integer

        MAtch:
        math
        dynamic programming
        array

        Plan:
        initialize two variable to store the two routes/ robbing approaches the bugler could take
        start from house 1 and be skipping a house or start at the second house and stll skip a house
        compare the max steals he can get from either approaches
        then return the second 

        R/E:
        s/c = O(1)
        t/c = O(N) 

        """
           # Special handling for empty case.
        if not nums:
            return 0

        elif len(nums) == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(second, first + nums[i])
            first = second
            second = curr

        return second
        