class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        visit = set()
        q = deque()

        rows, cols = len(grid) , len(grid[0])

        def addroom(r , c):

            if (r < 0 or r == rows or c < 0 or c == cols or 
                (r,c) in visit or grid[r][c] == -1):
                return

            q.append([r,c])
            visit.add((r,c))
            

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        dist = 0

        while q:
            
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                addroom(r + 1 , c)
                addroom(r - 1 , c)
                addroom(r , c + 1)
                addroom(r , c - 1)

            dist += 1

 
