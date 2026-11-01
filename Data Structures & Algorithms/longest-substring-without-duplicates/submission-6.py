class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet =set()
        lenS = len(s)
        maxLen = 0
        l=r=0

        while r < lenS:

            while r<lenS and s[r] not in charSet:
                charSet.add(s[r])
                r += 1

            maxLen = max(maxLen, r-l)

            if r<lenS:
                while s[r] != s[l]:
                    charSet.remove(s[l])
                    l += 1
                l+=1

            r += 1
        return maxLen