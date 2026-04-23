class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stk = []

        for a in asteroids:

            while stk and a < 0 and stk[-1] > 0:

                if stk[-1] > abs(a):
                    a = 0
                
                elif stk[-1] == abs(a):
                    a = 0 
                    stk.pop()
                
                else:
                    stk.pop()

            if a!=0:
                stk.append(a)
        
        return stk