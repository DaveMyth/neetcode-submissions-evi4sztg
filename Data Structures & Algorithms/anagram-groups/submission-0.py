class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        charCtrArr = []
        groupArr = []
        charLenArr = []

        for word in strs:
            matchFound = False
            charCtr = [0]*26
            for c in word:
                charCtr[ord(c)-ord('a')] += 1

            for idx, group in enumerate(groupArr):
                if(charLenArr[idx] == len(word)):
                    charCtrCpy = charCtr.copy()
                    for idx,val in enumerate(charCtrArr[idx]):
                        charCtrCpy[idx] -= val
                    if(not(any(charCtrCpy))):
                        group.append(word)
                        matchFound = True
                        break
            if(not matchFound):
                charCtrArr.append(charCtr)
                charLenArr.append(len(word))
                groupArr.append([word])

        return groupArr
