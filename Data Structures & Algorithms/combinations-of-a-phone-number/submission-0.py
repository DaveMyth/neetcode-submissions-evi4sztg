class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        keyPad = {'2': ["a", "b", "c"], '3': ["d", "e", "f"], '4': ["g", "h", "i"], '5': ["j", "k", "l"], '6': ["m", "n", "o"], '7': ["p", "q", "r", "s"], '8': ["t", "u", "v"], '9': ["w", "x", "y", "z"]}

        def helper(currIdx: int, currStr: str):

            if currIdx == len(digits):
                res.append(currStr)
                return

            for letter in keyPad[digits[currIdx]]:
                helper(currIdx + 1, currStr + letter)

        if len(digits) == 0:
            return []

        helper(0, "")
        return res