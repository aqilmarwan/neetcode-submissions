class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)