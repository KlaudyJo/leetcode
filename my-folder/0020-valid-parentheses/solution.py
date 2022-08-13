class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        
        brack, stack ={'(':')', '{': '}', '[': ']'}, []
        for b in s:
            if not stack or stack[-1] not in brack or brack[stack[-1]] != b:
                stack.append(b)
            else:
                stack.pop()
        return True if not stack else False
                
