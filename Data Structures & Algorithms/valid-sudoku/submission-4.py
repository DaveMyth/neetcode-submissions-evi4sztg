class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowSet = {}
        colSet = {}
        boxSet = {}
        
        for ctr1 in range(9):
            for ctr2 in range(9):
                val = board[ctr1][ctr2]
                if val == '.':
                    continue

                rIdx,cIdx = ctr1//3, ctr2//3
                boxIdx = tuple((rIdx, cIdx))

                if (ctr1 in rowSet and val in rowSet[ctr1]) or (ctr2 in colSet and val in colSet[ctr2]) or (boxIdx in boxSet and val in boxSet[boxIdx]):
                    return False

                if ctr1 not in rowSet:
                    rowSet[ctr1] = set()
                if ctr2 not in colSet:
                    colSet[ctr2] = set()
                if boxIdx not in boxSet:
                    boxSet[boxIdx] = set()
                    
                rowSet[ctr1].add(val)
                colSet[ctr2].add(val)
                boxSet[boxIdx].add(val)

        return True