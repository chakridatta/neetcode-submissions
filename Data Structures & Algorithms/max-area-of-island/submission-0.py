class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        max_area = 0

        def bfs(r, c):

            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            area = 1  # count starting cell

            while q:

                row, col = q.popleft()

                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr, dc in directions:

                    nr, nc = row + dr, col + dc

                    if (nr in range(rows) and
                        nc in range(cols) and
                        (nr, nc) not in visit and
                        grid[nr][nc] == 1):

                        area += 1
                        q.append((nr, nc))
                        visit.add((nr, nc))

            return area

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, bfs(r, c))

        return max_area