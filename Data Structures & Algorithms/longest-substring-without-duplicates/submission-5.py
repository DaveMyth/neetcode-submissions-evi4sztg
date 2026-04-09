class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        l=r=0
        maxLen = 0

        while(r<len(s)):
            while(r<len(s) and s[r] not in charSet):
                charSet.add(s[r])
                r += 1
            
            maxLen = max(maxLen, r-l)

            if(r<len(s)):
                while(s[l]!=s[r]):
                    print(l,str(charSet))
                    charSet.remove(s[l])
                    l += 1
                charSet.remove(s[l])
                l+=1

        return maxLen