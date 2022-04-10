class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if  len(s) != len(t):
            return False
        
        #create a hashmap
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for j in countS:
            if countS[j] != countT.get(j, 0):
                return False
        return True