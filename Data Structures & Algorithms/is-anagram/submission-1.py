class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for char in s:
            countS[char] = countS.get(char,0) + 1
        countT = {}
        for char in t:
            countT[char] = countT.get(char,0) + 1
        if countS == countT:
            return True
        return False