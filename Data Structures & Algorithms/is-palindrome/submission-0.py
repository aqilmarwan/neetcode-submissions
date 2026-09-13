class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pattern matching in haskell, match [-1] == [1]
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
                