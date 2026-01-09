class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Match:
        backtrack using dfs/recursion

        Plan:
        start with a temp subset thats empty
        recursively update subset by either including or excluding an element
        then backtrack by popping current element

        R/E:
        s/c = O(n)
        t/c = O(n*2^n) - 
        """
        def dfs(i):
            if i == len(nums):
                #add copy of the subset
                res.append(temp[:])
                return 

            #exclude curr element
            dfs(i+1)

            #include curr element
            temp.append(nums[i])
            dfs(i+1)

            #backtrack by removing curr element
            temp.pop()

        res, temp = [], []

        dfs(0)

        return res