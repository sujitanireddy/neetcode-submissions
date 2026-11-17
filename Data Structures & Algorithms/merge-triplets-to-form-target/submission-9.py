"""
good_values = set(0,1,2) len == 3: return True

triplets = [[2,5,6],[1,4,4],[5,7,5]]
target = [5,4,6]
"""




class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = set()

        for triplet in triplets:

            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i in range(3):
                if triplet[i] == target[i]:
                    good.add(i)
        
        return len(good) == 3