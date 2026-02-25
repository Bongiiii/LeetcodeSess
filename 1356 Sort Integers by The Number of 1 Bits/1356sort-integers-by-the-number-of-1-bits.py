class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        iterate through arr, take each num and convert to bits but dont store,
         just continue counting 1s in the bit rep
        then be storing, the original num and corresponding 1bit count
         as a key-value pair in a dictionary
        then sort using the values and return sorted list 

        #what about duplicates
        """
        #using built in bit count func
        return sorted(arr, key = lambda x: (x.bit_count(), x))
