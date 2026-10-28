class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for string in strs:

            charCtr = [0]*26

            for c in string:
                charCtr[ord(c)-97] += 1
            
            charCtr = tuple(charCtr)
            if(charCtr in res):
                res[charCtr].append(string)
            else:
                res[charCtr] = [string]

        return list(res.values())

