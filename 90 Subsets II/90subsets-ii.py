class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Similar to #78 difference is that they have duplicates
        so i will sort the array to keep duplicates consecutively and skip when a number is encountered
        still include elements
        exclude an element and all its duplicates
        backtrack, and remove the element

        """
        nums.sort()

        def dfs(i):

            #base case
            if i == len(nums):
                #copy current subset
                res.append(temp[:])
                return

            #include current element
            temp.append(nums[i])
            dfs(i+1)

            #backtrack and remove current element
            num = temp.pop()
            #exclude current element
            while i+1 < len(nums) and nums[i+1] == num:
                i+=1
                
            #explore without all the duplicates
            dfs(i+1)


        temp, res = [], []

        #recursively call helper on whole list
        dfs(0)

        return res