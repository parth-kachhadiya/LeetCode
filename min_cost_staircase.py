class Solution:
    def minCostClimbingStairs(self, cost:list):
        n = len(cost)-2
        cost.append(0)

        while n != -1:
            cost[n] = min(cost[n + 1], cost[n + 2]) + cost[n]
            n -= 1

        return min(cost[0],cost[1])
    
print(Solution().minCostClimbingStairs([0,2,2,1]))