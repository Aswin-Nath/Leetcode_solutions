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