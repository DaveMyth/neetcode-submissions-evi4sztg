class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currPart = []

        def helper(currIdx: int) -> None:

            if currIdx >= len(s):
                res.append(currPart.copy())
                return

            for i in range(currIdx, len(s)):
                if self.isPali(s, currIdx, i):
                    currPart.append(s[currIdx:i+1])
                    helper(i + 1)
                    currPart.pop()

        helper(0)

        return res

    def isPali(self, s, l, r):

        while l < r:
            if s[l]!=s[r]:
                return False

            l+=1
            r-=1

        return True