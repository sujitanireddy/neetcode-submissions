from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = collections.defaultdict(int)
        output = []

        for num in nums:
            freq[num] += 1
        
        sorted_freq = sorted(freq.items(), key = lambda x: x[1],  reverse = True)

        print(sorted_freq)
        for i in range(k):
            output.append(sorted_freq[i][0])

        return output
            
