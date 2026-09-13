class Solution:
    def isValid(self, s: str) -> bool:
        #stack 
        stack = []
        hashMap = { "}" : "{", "]" : "[", ")" : "("}


        for pair in s:
            # if close paranthesis
            if pair in hashMap:
                if stack and stack[-1] == hashMap[pair]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(pair)
        return True if not stack else False