class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #using bisect_right to do the binary search

        index = bisect_right(letters, target)

        return letters[index%len(letters)]