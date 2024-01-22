class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        stack=[]
        dp=[0]*n
        mod= 10**9 + 7
        ans=0
        for i in range(n):
            while(stack and arr[stack[-1]]>arr[i]):
                stack.pop()
            if stack:
                ind=stack[-1]
                dp[i]=dp[ind]+arr[i]*(i-ind)
            else:
                dp[i]=arr[i]*(i+1)
            stack.append(i)
            ans=(ans+dp[i])%mod
        return ans