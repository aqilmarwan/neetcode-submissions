class Solution:
    def climbStairs(self, n: int) -> int:
        
        # 1 or 2 steps
        #  i + 1 or i + 2

        def dfs(i):
            if i >= n:
                return i == n # reached the top
            return (dfs(i + 1) + dfs(i + 2))

        return dfs(0)