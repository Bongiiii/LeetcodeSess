class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Understand:
        input - array of integers, output - array of arrays

        Match:
        math
        array manipulation
        permutations
        backtracking

        Plan:
        initiate an array to store resultant array
        have a helper function to permutate the array


        R/E:
        s/c = O(N * (N-1))
        t/c = 
        """
        #array to store resultant array of arrays
        res = []


        #helper function to recursively backtrack and find permutations of nums
        def permuteHelper(variation):
            #base case, variations len is already same length as nums
            if len(variation) == len(nums):
                res.append(variation[:])
                return 

            #still need to build permutations
            for num in nums:
                #use the numbers that have not been used
                if num not in variation:
                    variation.append(num)
                    permuteHelper(variation)
                    #remove that number and try another
                    variation.pop()
                    
        #iitialize the variation array
        permuteHelper([])
        return res