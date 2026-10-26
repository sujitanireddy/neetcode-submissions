"""
if any value in triplet is > target then there is no point you will dominate

if not check if relative positions is same, if yes then mark them and return if the markings are 3

[1,2,3]
[7,1,1]


[7,2,3]


"""
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = set()

        for t in triplets:

            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i in range(len(t)):

                if t[i] == target[i]:

                    good.add(i)
        
        return len(good) == 3