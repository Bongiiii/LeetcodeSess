class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Understand:
        iinput - string, output - array of strings

        Match:
        string manipuulation
        hashmap
        simulation

        Plan:
        map the numbers to the letters they have, like a key(number) and value(combination) pair
        then use the letters from each number and make combinations using the characters
        initiate an array that keeps the combinations found
        base case, empty string and when you encounter 1, skip as 1 doesn't map to any letter

        R/E:
        s/c = O(3N) = 3 * N - len of digits
        t/c = O(N) - 3 * len of digits
        """
        #output array
        res = ['']

        #mapping
        numCharMap = { "2": "abc", "3":"def", "4":"ghi", "5":"jkl", 
                        "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"
                    }

        #base case
        if not digits:
            return []

        for digit in digits:
            letters = numCharMap[digit]

            res = [prefix + letter for prefix in res for letter in letters]


        return res
        