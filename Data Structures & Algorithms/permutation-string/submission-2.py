class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = r = 0
        charCtrMap = {}

        #Go through s1 and keep character count
        for c in s1:
            charCtrMap[c] = 1 + charCtrMap.get(c,0)

        #Go through s2 in sliding windows to check if the same map of characters exists
        while(l< len(s2) and r<len(s2)):
            if(s2[l] not in charCtrMap):
                l += 1
                continue
            r = l

            while(r<len(s2) and charCtrMap.get(s2[r],0)>0):
                charCtrMap[s2[r]] -= 1
                r += 1
                if(sum(charCtrMap.values()) == 0):
                    return True
                
            for ctr in range(l,r):
                charCtrMap[s2[ctr]] += 1
            l+=1

            
        return False