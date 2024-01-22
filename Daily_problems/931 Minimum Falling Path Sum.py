Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:



Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

# solution
class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        dp=[[0]*(n) for i in range(m)]
        dp[0]=mat[0]
        for i in range(1,m):
            for j in range(n):
                dp[i][j]=mat[i][j]+min(dp[i-1][j],dp[i-1][max(0,j-1)],dp[i-1][min(n-1,j+1)])
        return min(dp[-1])
