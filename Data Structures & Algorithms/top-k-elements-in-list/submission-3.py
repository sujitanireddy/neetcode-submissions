class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = defaultdict(int)

        for number in nums:
            hashmap[number] += 1
        
        return sorted(hashmap.keys(), reverse=True, key= lambda x: hashmap[x])[:k]