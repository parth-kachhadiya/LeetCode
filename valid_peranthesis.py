class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length == 1 or length == 0:
            return False
        else:
            peranthesis = []
            for bracket in s:
                l2 = len(peranthesis)
                if bracket == '(' or bracket == '[' or bracket == '{':
                    peranthesis.append(bracket)
                elif bracket == ')' and l2 != 0:
                    if peranthesis[-1] == '(':
                        peranthesis.pop()
                    else:
                        return False
                elif bracket == ']' and l2 != 0:
                    if peranthesis[-1] == '[':
                        peranthesis.pop()
                    else:
                        return False
                elif bracket == '}' and l2 != 0:
                    if peranthesis[-1] == '{':
                        peranthesis.pop()
                    else:
                        return False
                else:
                    return False
                    
            return True if len(peranthesis) == 0 else False