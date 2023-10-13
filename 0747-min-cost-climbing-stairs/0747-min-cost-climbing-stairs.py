class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first=cost[0]
        second=cost[1]
        n=len(cost)
        dp = [cost[0],cost[1]]
        for i in range(2,n):
            dp.append(cost[i]+min(dp[i-1],dp[i-2]))
        return min(dp[n-1],dp[n-2])