class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
        hashmap = {num:freq} TC: O(nlogn) SC: O(n)

        can we reduce the TC? 

        hashmap = {num:freq}

        freq buckets
         
         0  1.  2.  3  4. 5. 6
        [[][],[2],[3],[],[],[]]

        """
        num_freq_map = defaultdict(int)

        for num in nums:
            num_freq_map[num] += 1
        
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        
        for num, freq in num_freq_map.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                for val in bucket[i]:
                    res.append(val)

            if len(res) == k:
                return res
