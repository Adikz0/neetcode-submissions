class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        lastLetter = len(s) -1
        firstLetter = 0

        while firstLetter <= lastLetter:
            while firstLetter <= lastLetter and s[firstLetter].isalnum() == False:
                firstLetter+=1

            while lastLetter >= firstLetter and s[lastLetter].isalnum() == False:
                lastLetter -= 1

            if firstLetter <= lastLetter and s[firstLetter] != s[lastLetter] :
                return False
            else:
                firstLetter+=1
                lastLetter-= 1
        return True