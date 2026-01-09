class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        
        """
        def dfs(i):
            if i >= len(nums):
                #add a copy of subset
                res.append(temp[:])
                return

            for j, num in enumerate(nums):
                if not used[j]:
                    #mark as used
                    used[j] = True

                    #add current element to subset
                    temp[i] = num

                    #recursively fill the next position
                    dfs(i+1)

                    #mark as unused
                    used[j] = False

        temp, res, used = [0] * len(nums), [], [False] * len(nums)
        dfs(0)

        return res
