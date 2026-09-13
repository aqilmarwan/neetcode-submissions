class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Check if sub-array started from [0] = True, else False
        # if True, stop or add nums[i] and recurse
        # if False, skip current nums[i] or make current nums[i] as starting
        # Base - if i is at end, return 0 or return at least [0]

        def dfs(i, flag):
            if i == len(nums):
                return 0 if flag else -1e6
            elif flag:
                return max(0, nums[i] + dfs(i + 1, True))
            
            return max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
        return dfs(0, False)



