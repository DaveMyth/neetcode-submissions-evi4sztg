class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        charCtr = [0] * 26

        for ctr in range(len(s)):
            charCtr[ord(s[ctr])-97] += 1
            charCtr[ord(t[ctr])-97] -= 1

        for ctr in range(26):
            if charCtr[ctr] != 0:
                return False


        return True