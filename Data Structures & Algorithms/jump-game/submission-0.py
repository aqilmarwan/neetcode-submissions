class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # for nums[i], always jumps i + nums[i]
        # if nums[-1] is not equal to res, then False
        # else nums[-1] is     equal to res, then True

        def dfs(i):
            if i == len(nums) - 1:
                return True
            
            end = min(len(nums) - 1, i + nums[i]) # cap the index at min
            for j in range(i + 1, end + 1): # range of all possible start and end i, 
                if dfs(j):
                    return True
            return False
        return dfs(0)
