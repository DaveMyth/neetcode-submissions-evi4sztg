class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0]*26

        for c in s1:
            count[ord(c)-ord('a')]+=1
        
        l=r=0

        while(r<len(s2)):
            if(r-l+1>len(s1)):
                count[ord(s2[l])-ord('a')] += 1
                l += 1
                continue

            count[ord(s2[r])-ord('a')] -= 1
            if(not(any(count))):
                return True
            r += 1    

        return False
