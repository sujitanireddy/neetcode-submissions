class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        """
        2->   4->    <-4    <-1

        asteroid collides only when a +asteroid is there and then -ve. 

        3 conditions
            - Same size
            - -ve asteroid is bigger
            - -ve asterod is smaller

        TC: O(n)
        SC: O(n)
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

            if a!=0:
                stk.append(a)
        
        return stk

        

