class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # -> -> <- <-
        #[2, 4, 4, 1]

        #if the top of the stk is +ve and incoming asteroid is -ve - BOOM
            #3 conditions of collions
                #same - incoming and top of stk and poppped
                #< - incoming is popped
                #> - top of stk is popped

        stk = []
        for a in asteroids:
            while stk and stk[-1] > 0 and a < 0:
                if stk[-1] == abs(a):
                    stk.pop()
                    a = 0
                elif stk[-1] > abs(a):
                    a = 0
                else:
                    stk.pop()
            
            if a!=0:
                stk.append(a)
        
        return stk