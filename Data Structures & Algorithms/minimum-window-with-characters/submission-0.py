class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case when t is empty str
        if t == "":
            return ""
