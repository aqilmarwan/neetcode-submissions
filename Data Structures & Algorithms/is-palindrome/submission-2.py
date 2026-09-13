class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pattern matching in haskell, match [-1] == [1]
        newStr = ""

        for character in s:
            if character.isalnum():
                newStr += character.lower()
        return newStr == newStr[::-1]