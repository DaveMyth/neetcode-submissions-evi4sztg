class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False

        ctr = 0 
        charCtr = [0]*26
        while(ctr<len(s)):
            charCtr[ord(s[ctr])-97] += 1
            charCtr[ord(t[ctr])-97] -= 1
            ctr+=1

        if(any(charCtr)):
            return False
        return True