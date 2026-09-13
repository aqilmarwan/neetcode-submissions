class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums:
            if num is seen:
                return num
            seen.add(num)
        return -1
