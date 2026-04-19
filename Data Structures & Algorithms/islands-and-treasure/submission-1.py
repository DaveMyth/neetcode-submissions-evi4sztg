class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False]*COLS for ctr in range(ROWS)]
        q = deque()
        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        lvlZero = []

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visited[i][j] = True
                    lvlZero.append((i,j))
                if grid[i][j] == -1:
                    visited[i][j] = True
        q.append(lvlZero)
        levelCtr = 0
        
        while q:
            currLevel = q.popleft()
            nextLevel = []
            for step in currLevel:
                visited[step[0]][step[1]] = True
                grid[step[0]][step[1]] = min(grid[step[0]][step[1]], levelCtr)
                for move in moves:
                    i = step[0] + move[0]
                    j = step[1] + move[1]

                    if i>-1 and i<ROWS and j>-1 and j< COLS and not visited[i][j]:
                        nextLevel.append((i,j))
            if nextLevel:
                q.append(nextLevel)
                levelCtr += 1
                    
