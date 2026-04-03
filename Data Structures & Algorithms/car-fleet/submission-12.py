class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #algorithm
        #Zip pos and speed into a pair of lists and arrange in des order by pos
        #Using a stack keep computing the time and if time is fast then pop else keep adding. Return len(stk)

        stk = []
        pos_speed = list(zip(position, speed))
        pos_speed.sort(reverse=True)
        
        for pos, speed in pos_speed:

            time_taken = (target - pos) / speed

            stk.append(time_taken)

            if len(stk) >= 2 and stk[-1] <= stk[-2]:

                stk.pop() 
        
        return len(stk)