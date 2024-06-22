class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones) > 1):
            # Sort the stones in descending order
            stones.sort(reverse=True)
            # Take the two heaviest stones
            first = stones.pop(0)
            second = stones.pop(0)
            
            if first != second:
                # If they are not the same, push the difference back into the list
                stones.append(first - second)
        
        # If there is one stone left, return it, otherwise return 0
        return stones[0] if stones else 0
