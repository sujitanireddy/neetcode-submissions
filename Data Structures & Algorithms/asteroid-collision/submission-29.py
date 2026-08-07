class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        """

        2 -> 4 ->  <-4  <- 1

        <- ->

        smaller one explodes
        same size: both explode

        [[7,-3,9]]

        [7,]

        Observations: If the asteroid is -ve and top of stk is positive then only collision can occur.
        Compare top of stack and current astroid and write conditionals.

        """
        stk = []

        for a in asteroids:

            while stk and a < 0 and stk[-1] > 0:

                if stk[-1] == abs(a):
                    stk.pop()
                    a = 0
                
                elif stk[-1] > abs(a):
                    a = 0

                else:
                    stk.pop()            
            

            if a != 0:
                stk.append(a)

        return stk