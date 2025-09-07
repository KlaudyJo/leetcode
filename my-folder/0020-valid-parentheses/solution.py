class Solution:
    def isValid(self, s: str) -> bool:
        brack ={'(':')', '{': '}', '[': ']'}
        stk = []

        for c in s:
            if c in brack:
                stk.append(c)
            else:
                if not stk or brack[stk.pop()] != c:
                    return False
        return not stk


        
