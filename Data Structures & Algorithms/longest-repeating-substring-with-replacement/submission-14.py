class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charCount = {}
        r=l=0
        maxLen = 0
        maxF = 0

        while r < len(s):
            charCount[s[r]] = 1 + charCount.get(s[r],0)
            maxF = max(maxF, charCount[s[r]])
            
            if (r-l+1-maxF) <= k:
                maxLen = max(maxLen, r-l+1)

            while (r-l+1-maxF) > k:
                charCount[s[l]] -= 1
                l += 1
            r += 1

        return maxLen