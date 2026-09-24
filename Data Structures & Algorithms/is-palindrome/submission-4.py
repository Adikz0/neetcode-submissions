class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        firstLetter = 0
        lastLetter = len(s) - 1

        while firstLetter < lastLetter:

            if s[firstLetter].isalnum() == False:
                while s[firstLetter].isalnum() == False and firstLetter < lastLetter:
                    firstLetter += 1

            if s[lastLetter].isalnum() == False:
                while s[lastLetter].isalnum() == False and firstLetter < lastLetter:
                    lastLetter -= 1

            if s[firstLetter] == s[lastLetter]:
                firstLetter += 1
                lastLetter -= 1
            else:
                return False
            
            
        return True

        


        
