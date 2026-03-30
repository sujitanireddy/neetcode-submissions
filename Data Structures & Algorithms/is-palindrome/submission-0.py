class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ''
        for char in s:
            if char.isalnum():
                alphanum += char
        
        if alphanum.lower() == alphanum[::-1].lower():
            return True
        
        else:
            return False

        