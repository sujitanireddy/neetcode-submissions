class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        """
        Initate two pointers
        If it's not alphanum() then skip
        compare both L and R, if it's not same: return False
        L += 1
        R -= 1
        
         L                       R
        Was it a car or a cat I saw?


        """

        L = 0
        R = len(s) - 1

        while L < R:

            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True