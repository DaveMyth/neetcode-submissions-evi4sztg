class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruitCtr = 0
        q = deque()
        lvlZero = []
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False]*COLS for ctr in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fruitCtr += 1
                if grid[i][j] == 2:
                    lvlZero.append((i,j))
                    fruitCtr += 1
                    visited[i][j] = True
                if grid[i][j] == 0:
                    visited[i][j] = True
        q.append(lvlZero)

        time = 0
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        while q:
            print(grid)
            currLevel = q.popleft()
            nextLvl = []
            print(currLevel)
            for step in currLevel:
                fruitCtr -= 1
                for move in moves:
                    i = step[0] + move[0]
                    j = step[1] + move[1]

                    if i>-1 and i<ROWS and j>-1 and j<COLS and not visited[i][j]:
                        visited[i][j] = True
                        nextLvl.append((i,j))
            time += 1
            if nextLvl:
                q.append(nextLvl)
        print(grid)
        return -1 if fruitCtr > 0 else time-1