class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        """
        [2 -> ,4 -> , <- -4, <- -1]

        When does collison occur? 
            - +ve and -ve asteroids

        if size is same - both are removed
        if size is not the same - bigger one survives

        algorithm
        - If +ve add to the stk
        - If top of the stk is +ve and if incoming asteroid is -ve then - conditions check
        """

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

            if a != 0:
                stk.append(a)
        
        return stk
