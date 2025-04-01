from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for stri in strs:
            map = tuple(sorted(stri))

            anagrams[map].append(stri)

        return list(anagrams.values())