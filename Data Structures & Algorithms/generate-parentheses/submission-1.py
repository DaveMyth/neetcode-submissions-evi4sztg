class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(currStr: str, l, r):

            if (r<l):
                return 

            if r==0 and l==0:
                res.append(currStr)

            if l > 0:
                helper(currStr+"(", l-1, r)

            if r>0:
                helper(currStr+")", l, r-1)

        helper("", n, n)
        return res