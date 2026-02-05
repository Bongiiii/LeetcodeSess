class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        """
        U:
        input - integer array, output - integer array

        M:
        simulation
        array manipulation

        P:
        modulo operator % used to handle wrap arounds
        use the enumerate func so as to have the iindex and elem as we iterate

        I:
        R:
        E:
        """
        n = len(nums)
        res = [1] * n

        for i, num in enumerate(nums):
            if num == 0:
                res[i] = nums[i]

            else:
                #added extra n to handle negatives and in +ves that doesnt affect anything as (i+x+n)%n = (i+x)%n
                indx = (i + num + n) % n
                res[i] = nums[indx]
        return res