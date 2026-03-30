class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = collections.defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        sorted_hashmap = sorted(hashmap.items(), reverse = True, key = lambda x: x[1]) 

        output = []
        for i in range(k):
            output.append(sorted_hashmap[i][0])

        return output