class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        for r in range(len(s)):
            count [s[r]] = 1 + count.get.values([s[r]], 0)
            while (r - l + 1) - count > k:
                l += 1
                count[s[l]] -= 1 
            result = max(res, r - l + 1)
        return result
