class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
       #initialize hashmaps
        mapST,mapTS={},{}
        n=len(s)
        #iterating through the strings
        for j in range(n):
            c1,c2=s[j],t[j]

            if ((c1 in mapST and mapST[c1]!=c2) or (c2 in mapTS and mapTS[c2]!=c1)):
                return False
            
            mapST[c1] = c2
            mapTS[c2] = c1

        return True


