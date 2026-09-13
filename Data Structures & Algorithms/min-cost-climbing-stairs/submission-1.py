class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dfs(i + 1) or dfs(i + 2)
        # iter the dfs value position

        def dfs(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i + 1), dfs(i + 2))

        return min(dfs(1), dfs(0))
