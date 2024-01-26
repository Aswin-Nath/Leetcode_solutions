There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
 

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n

# solution



class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, sr: int, sc: int) -> int:
        memo={}
        v=set()
        mod=10**9 + 7
        @lru_cache(None)
        def dfs(i,j,no):
            if (i,j,no) in memo:
                return memo[(i,j,no)]
            if (i==-1 or j==-1 or i==m or j==n) and no>=0:
                return 1
            if i<0 or j<0 or i>m or j>n or no<0:
                return 0
            left=dfs(i,j-1,no-1)
            right=dfs(i,j+1,no-1)
            down=dfs(i+1,j,no-1)
            up=dfs(i-1,j,no-1)
            memo[(i,j,no)]=up+left+down+right
            return memo[(i,j,no)]%mod
        return dfs(sr,sc,maxMove)%mod
        
