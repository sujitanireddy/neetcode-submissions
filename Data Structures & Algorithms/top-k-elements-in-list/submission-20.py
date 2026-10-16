"""
 
[1,2,2,3,3,3], k = 2

{
    1 : 1
    2 : 2
    3 : 3
}

nlogn
  0. 1.  2   3  4  5  6
[[],[1],[2],[3],[],[],[]]

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for val in buckets[i]:
                    res.append(val)
                    if len(res) == k:
                        return res

