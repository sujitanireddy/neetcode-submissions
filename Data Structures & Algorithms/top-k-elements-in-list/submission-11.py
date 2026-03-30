class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}
        output = []

        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0  
            freq_dict[num] += 1

        return sorted(freq_dict, key=freq_dict.get, reverse=True)[:k]

        
        
        