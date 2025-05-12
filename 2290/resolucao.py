from collections import deque

class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        obstacles = [[float('inf')] * n for _ in range(m)]
        obstacles[0][0] = 0
        
        q = deque()
        q.append((0, 0))
        
        while q:
            i, j = q.popleft()
            
            if i == m - 1 and j == n - 1:
                return obstacles[i][j]
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    new_obs = obstacles[i][j] + grid[ni][nj]
                    
                    if new_obs < obstacles[ni][nj]:
                        obstacles[ni][nj] = new_obs
                        if grid[ni][nj] == 0:
                            q.appendleft((ni, nj))
                        else:
                            q.append((ni, nj))
        
        return obstacles[m-1][n-1]

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))  # 2
    print(sol.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))  # 0
    print(sol.minimumObstacles([[0,0,0],[0,0,0],[0,0,0]]))  # 0
    print(sol.minimumObstacles([[0,1,1],[1,1,1],[1,1,0]]))  # 3