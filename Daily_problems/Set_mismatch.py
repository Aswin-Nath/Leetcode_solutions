class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        dp=[0,0]
        for i in range(1,len(nums)+1):
            if c[i]==2:
                dp[0]=i
            elif i not in c:
                dp[1]=i
        return dp
