class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False

        charCtr = [0]*26
        for ctr in range(len(s)):
            charCtr[ord(s[ctr])-ord('a')] += 1
            charCtr[ord(t[ctr])-ord('a')] -= 1

        if(not(any(charCtr))):
            return True
        return False