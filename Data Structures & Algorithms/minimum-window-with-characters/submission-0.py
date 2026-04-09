class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ctrMap = {}

        for c in t:
            ctrMap[c] = 1 + ctrMap.get(c,0)

        minLen = float("inf")
        minStr = ""
        completeCtr = len(ctrMap.keys())
        l=r=0

        while(r<len(s)):
            if(s[r] in ctrMap):
                ctrMap[s[r]] -= 1
                if(ctrMap[s[r]] == 0):
                    completeCtr -= 1
                
                while(completeCtr == 0):
                    if(minLen>r-l+1):
                        minStr = s[l:r+1]
                        minLen = r-l+1

                    if(s[l] in ctrMap):
                        ctrMap[s[l]] += 1
                        if(ctrMap[s[l]]>0):
                            completeCtr += 1
                    l += 1
            r+=1

        return minStr 

