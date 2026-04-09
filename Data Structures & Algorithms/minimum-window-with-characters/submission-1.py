class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l=r=0
        charCtrMap = {}
        minLen = float("inf")
        minStr = ""

        for c in t:
            charCtrMap[c] = 1 + charCtrMap.get(c,0)

        charComplCtr = len(list(charCtrMap.keys()))

        l=r=0

        while(r<len(s)):

            if(s[r] in charCtrMap):
                charCtrMap[s[r]] -= 1
                if(charCtrMap[s[r]] == 0):
                    charComplCtr -= 1
                    while(charComplCtr == 0):
                        if(minLen > r-l+1):
                            minLen = r-l+1
                            minStr = s[l:r+1]
                        
                        if(s[l] in charCtrMap):
                            charCtrMap[s[l]] += 1
                            if(charCtrMap[s[l]] == 1):
                                charComplCtr += 1
                        l += 1
            r += 1

        return minStr