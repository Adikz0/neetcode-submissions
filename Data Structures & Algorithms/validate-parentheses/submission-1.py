class Solution:
    def isValid(self, s: str) -> bool:
        map = {"]" : "[", ")" : "(", "}" : "{"}
        stk = []

        for p in s:
            if p not in map:
                stk.append(p)
            else:
                if stk:
                    x = stk.pop()
                    if x == map[p]:
                        continue
                    else:
                        return False
                else:
                    return False
        if not stk:
            return True
        else:
            return False
        
        