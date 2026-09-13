class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use hash set to store all int
        # if i has left neighbor(nums - 1) == update longest, and continue N + 1 until no right neighbor in set
        # for every i continue until i == end

        numSet = set(nums)
        total = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0 
                while (n + 1) in numSet:
                    length += 1
                total = max(length, total)
        return total


