class Solution:
    def isValid(self, s: str) -> bool:
        map = {"}":"{", ")":"(", "]":"["}

        stk = []

        for p in s:
            if p not in map:
                stk.append(p)

            elif p in map:
                if len(stk) == 0:
                    return False
                
                x = stk.pop()
                if map[p] == x:
                    continue
                else:
                    return False
        
        if len(stk) == 0:
            return True
        else:
            return False
        
        
        