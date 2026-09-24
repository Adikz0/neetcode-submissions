class Solution:
    def isPalindrome(self, s: str) -> bool:
        
     s = s.lower()

     firstWord = 0
     lastWord = len(s) - 1

     while firstWord < lastWord:


        if s[firstWord].isalnum() == False:
            while s[firstWord].isalnum() == False and firstWord < lastWord:
                firstWord += 1
        
        if s[lastWord].isalnum() == False:
            while s[lastWord].isalnum() == False and firstWord < lastWord:
                lastWord -=1 

        if s[firstWord] != s[lastWord]:
            return False
        elif s[firstWord] == s[lastWord]:
            firstWord += 1
            lastWord -= 1
     return True










        



