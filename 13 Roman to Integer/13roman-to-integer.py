class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Understand:
        input - string,  output - integer

        Match:
        math
        hashmap

        Plan:
        initiate a dictionary that maps roman numeral symbol to integer value pair
        initiate two variables, prevValue and currSum to 0
        reverse the string
        when the value is less than the prevValue, subtract value from currSum else increment with the value
        update prevValue to value
        then iterate through each character in string and extracting its value and summing it up
        finally return currSum

        R/E:
        s/c = O(N)
        t/c = O(N)
        """
        riDict = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }

        prevValue, currSum = 0, 0

        #s.reverse()

        for char in reversed(s):
            value = riDict[char]

            if value < prevValue:
                currSum -= value

            else:
                currSum += value

            prevValue = value

        return currSum