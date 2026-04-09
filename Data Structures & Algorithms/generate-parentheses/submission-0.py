class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        
        def helper(currStr: str,l: int, r: int) -> List[str]:
            if(r<l):
                return

            if(l==0 and r==0):
                self.res.append(currStr)
                return

            if(l>0):
                helper(currStr+"(", l-1, r)
            if(r>0):
                helper(currStr+")", l, r-1)

        helper("",n,n)
        return self.res