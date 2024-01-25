class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[1]*(n+1)
        ma=1
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
            ma=max(dp[i],ma)
        print(dp)
        return ma>=3
