class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['']
        len = 0
        for c in s:
            if(c == '(' or c == '{' or c == '['):
                stack.append(c)
                len+= 1
            elif(c==')' and stack[len] == '('):
                stack.pop()
                len-= 1
            elif(c==']' and stack[len] == '['):
                stack.pop()
                len-= 1
            elif(c=='}' and stack[len] == '{'):
                stack.pop()
                len-= 1
            else:
                return False
        if(len == 0):
            return True
        return False
