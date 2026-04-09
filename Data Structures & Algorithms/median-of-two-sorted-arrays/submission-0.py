class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #find min of two arrays (A)
        A, B = nums1, nums2
        totalLen = len(nums1) + len(nums2)
        half = totalLen // 2

        if(len(A) > len(B)):
            A, B = B, A

        #find a left partition in the smaller array (lpA)
        l, r = 0, len(A) - 1

        while True:
            lpA = (l+r)//2
        #left partition of bigger array is half - lpA
            lpB = half - lpA - 2
        #identify the partition markers
            Aleft = A[lpA] if lpA >= 0 else float("-inf")
            Bleft = B[lpB] if lpB >= 0 else float("-inf")
            Aright = A[lpA+1] if lpA+1 < len(A) else float("inf")
            Bright = B[lpB+1] if lpB+1 < len(B) else float("inf")
        #Check if lpA <= lpB+1 and lpB <= lpA+1
            if(Aleft <= Bright and Bleft <= Aright):
        #if so, the partition is correct
                #odd 
                if(totalLen % 2):
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        #if not, adjust the partitions accordingly
            elif Aleft > Bright:
                r = lpA-1
            else:
                l = lpA + 1