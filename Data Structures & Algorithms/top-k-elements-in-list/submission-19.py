class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
        Bucket Sort
        
        { 
         1 : 2
         3: 4
         2: 5
         }

         0  1   2.  3   4  5
        [[] [1] [2] [3] []  []]

        """

        freq = defaultdict(int)

        for val in nums:
            freq[val] += 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        for val, freq in freq.items():
            buckets[freq].append(val)

        output = []

        for i in range(len(buckets)-1, -1 ,-1):
            
            if buckets[i]:
                for val in buckets[i]:
                    output.append(val)

                    if len(output) == k:
                        return output

        





