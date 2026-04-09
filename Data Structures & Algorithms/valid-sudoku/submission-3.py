class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = {}
        colSet = {}
        boxSet = {}

        for ctr1 in range(9):
            for ctr2 in range(9):
                if(board[ctr1][ctr2] == '.'):
                    continue
                    
                boxRIdx = ctr1//3
                boxCIdx = ctr2//3
                combIdx = str(boxRIdx)+","+str(boxCIdx)

                if(ctr1 not in rowSet):
                    rowSet[ctr1] = set(board[ctr1][ctr2])
                elif(board[ctr1][ctr2] in rowSet[ctr1]):
                    return False
                else:
                    rowSet[ctr1].add(board[ctr1][ctr2])

                if(ctr2 not in colSet):
                    colSet[ctr2] = set(board[ctr1][ctr2])
                elif(board[ctr1][ctr2] in colSet[ctr2]):
                    return False
                else:
                    colSet[ctr2].add(board[ctr1][ctr2])

                if(combIdx not in boxSet):
                    boxSet[combIdx] = set(board[ctr1][ctr2])
                elif(board[ctr1][ctr2] in boxSet[combIdx]):
                    return False
                else:
                    boxSet[combIdx].add(board[ctr1][ctr2])

        return True