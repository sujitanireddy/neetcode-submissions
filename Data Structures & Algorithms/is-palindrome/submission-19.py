class Solution:
    def isPalindrome(self, s: str) -> bool:

        """ 
        "Was it a car or a cat I saw?" 
          L                        R

        """
        
        L = 0
        R = len(s) - 1

        while L < R:

            while L < R and s[L].isalnum() == False:
                L += 1
            
            while L < R and s[R].isalnum() == False:
                R -= 1
            
            if s[R].lower() != s[L].lower():
                print(s[R], s[L])
                return False
            
            else:
                R -= 1
                L += 1

        return True