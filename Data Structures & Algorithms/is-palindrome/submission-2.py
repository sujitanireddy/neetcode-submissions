class Solution:
    def isPalindrome(self, s: str) -> bool:

        reversed_s = ''
        for i in range(len(s) - 1, -1 , -1):
            if s[i].isalpha() or s[i].isdigit():
                reversed_s += s[i]

        stripped_s = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                stripped_s += s[i]

        print(reversed_s.lower())
        print(stripped_s.lower())
        
        if stripped_s.lower() == reversed_s.lower():
            return True
        else:
            return False

        