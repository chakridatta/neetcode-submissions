class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        visit = set()

        rows = len(grid)
        cols = len(grid[0])

        fresh = 0

        def rotten(r, c ):

            nonlocal fresh

            if ( r < 0 or r == rows or c < 0 or c == cols 
                or (r, c) in visit or grid[r][c] != 1):
                return
            
            fresh -= 1
            q.append([r,c])
            visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))

        minute = 0

        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                rotten(r + 1, c )
                rotten(r - 1, c )
                rotten(r , c + 1)
                rotten(r , c - 1)

            minute += 1

        return -1 if fresh > 0 else minute

