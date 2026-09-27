class Solution:
    def isValid(self, s: str) -> bool:
        map = {"}":"{", ")":"(", "]" : "["}

        stk = []

        for p in s:
            if p not in map:
                stk.append(p)
            else:
                if len(stk) != 0:
                    x = stk.pop()
                    if x == map[p]:
                        continue
                    else:
                        return False    
                else:
                    return False
        if len(stk) == 0:
            return True
        else:
            return False