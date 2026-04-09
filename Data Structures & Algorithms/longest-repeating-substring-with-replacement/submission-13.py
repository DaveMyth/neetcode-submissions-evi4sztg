class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l=r=0
        charCountMap = {}
        maxLen = 0
        maxF = 0

        while(r<len(s)):
            charCountMap[s[r]] = charCountMap.get(s[r],0) + 1
            maxF = max(maxF, charCountMap[s[r]])
            if(r-l+1-maxF<=k):
                maxLen = max(maxLen, r-l+1)
                r+=1
                continue

            while(r-l+1-maxF>k):
                charCountMap[s[l]] -= 1
                l += 1
            r += 1

        return maxLen