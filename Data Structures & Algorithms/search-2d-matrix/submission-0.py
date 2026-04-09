class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1,r1= 0,len(matrix)-1

        while(l1<=r1):
            mid1 = (l1+r1)//2
            l2,r2 = 0,len(matrix[0])-1

            while(l2<=r2):

                if(l2>0 and target<matrix[mid1][l2] or r2<len(matrix[0])-1 and target>matrix[mid1][r2]):
                    return False
                    
                mid2 = (l2+r2)//2
                if(matrix[mid1][mid2]==target):
                    return True
                if(matrix[mid1][mid2]>target):
                    r2 = mid2-1
                elif(matrix[mid1][mid2]<target):
                    l2 = mid2+1
            if(matrix[mid1][0]>target):
                r1 = mid1-1
            elif(matrix[mid1][-1]<target):
                l1 = mid1+1

        return False

        [[1,3,5,7],[10,11,16,20],[23,30,34,60]]