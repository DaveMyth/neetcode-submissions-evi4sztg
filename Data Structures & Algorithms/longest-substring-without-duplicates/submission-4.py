class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l=r=0
        maxLen = 0

        while(r<len(s)):
            currSub = s[l:r+1]
            print(currSub)
            while(l<r and s[r] in currSub[:-1]):
                l+=1
                currSub = s[l:r+1]
            if(r-l+1>maxLen):
                maxLen = r-l+1
            r+=1

        return maxLen