class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num is seen:
                return True
            seen.add();
        return False
        