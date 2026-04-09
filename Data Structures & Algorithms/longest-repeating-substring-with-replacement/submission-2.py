class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charCountMap = {}
        maxLen = 0
        l=r=0
        modeChar = ''
        while(r<len(s)):
            if(s[r] not in charCountMap):
                charCountMap[s[r]] = 0

            charCountMap[s[r]]+=1

            while(r-l+1-max(charCountMap.values())>k):
                charCountMap[s[l]] -=1
                l += 1
            
            maxLen = max(r-l+1, maxLen)
            r+=1

            # modeChar = max(charCountMap.keys(), key=lambda x: charCountMap[x])
            # if(r-l+1-charCountMap[modeChar]<=k):
            #     maxLen = max(r-l+1, maxLen)
            #     r+=1
            #     continue

            # while(r-l+1-charCountMap[modeChar]>k):
            #     charCountMap[s[l]]-=1 
            #     l+=1             
            #     modeChar = max(charCountMap.keys(), key=lambda x: charCountMap[x])

        return maxLen