class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l=r=0
        charCountMap = {}
        maxLen = 0

        while(r<len(s)):
            charCountMap[s[r]] = charCountMap.get(s[r],0) + 1
            if(r-l+1-max(list(charCountMap.values()))<=k):
                maxLen = max(maxLen, r-l+1)
                r+=1
                continue

            while(r-l+1-max(list(charCountMap.values()))>k):
                charCountMap[s[l]] -= 1
                l += 1
            r += 1

        return maxLen