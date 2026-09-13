class Solution:
    def jump(self, nums: List[int]) -> int:
        # for every range i, j 

        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')

            end = min(len(nums) - 1, i + nums[i]) # caps to min index jump from nums
            res = float('inf')

            for j in range(i + 1, end + 1):
                res = min(res, 1 + dfs(j))
            return res
        return dfs(0)