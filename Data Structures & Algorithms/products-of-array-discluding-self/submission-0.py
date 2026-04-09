class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        leftProd = [1]*length
        rightProd = [1]*length
        zCounter = 0

        for ctr in range(length):

            if(ctr==0):
                leftProd[0] = nums[0]
                rightProd[length-1] = nums[length-1]
                continue

            if(nums[ctr] != 0):
                leftProd[ctr] = leftProd[ctr-1] * nums[ctr]
            else:
                zCounter += 1
                leftProd[ctr] = leftProd[ctr-1]

            if(nums[length-ctr-1] != 0):
                rightProd[length-ctr-1] = rightProd[length-ctr] * nums[length-ctr-1]
            else:
                rightProd[length-ctr-1] = rightProd[length-ctr]

        res = []
        for ctr in range(length):
            if(ctr>0 and ctr<length-1):
                res.append(leftProd[ctr-1]*rightProd[ctr+1])
            elif(ctr>0):
                res.append(leftProd[ctr-1])
            elif(ctr<length-1):
                res.append(rightProd[ctr+1])

        if(zCounter>1):
            return [0]*length

        elif(zCounter==1):
            for ctr in range(len(nums)):
                if(nums[ctr] != 0):
                    res[ctr] = 0

        return res

