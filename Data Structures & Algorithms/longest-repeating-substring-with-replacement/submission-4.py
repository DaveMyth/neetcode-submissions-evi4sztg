class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charCountMap = {}
        maxLen = 0
        l=r=0
        maxF = 0
        while(r<len(s)):
           
            if(s[r] not in charCountMap):
                charCountMap[s[r]] = 0

            charCountMap[s[r]]+=1
            maxF = max(maxF, charCountMap[s[r]])
            while(r-l+1-maxF>k):
                charCountMap[s[l]] -=1
                l += 1
            
            maxLen = max(r-l+1, maxLen)
            r+=1

        return maxLen