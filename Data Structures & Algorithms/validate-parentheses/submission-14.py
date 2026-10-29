class Solution:
    def isValid(self, s: str) -> bool:

        map = {"}" : "{" , ")" :"(", "]" : "["}
        stk = []
        
        for parenthesis in s:
            if parenthesis not in map:
                stk.append(parenthesis)
            elif parenthesis in map:
                if len(stk) == 0:
                    return False
                else:
                    x = stk.pop()
                    if map[parenthesis] == x:
                        continue
                    else:
                        return False

        if len(stk) == 0:
            return True
        else:
            return False

