class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        self.count = 0
        cache = {}

        def recurse(i):

            if i >= n:
                return 1

            if i in cache:
                return cache[i]

            if s[i] == "0":
                return 0

            cache[i] = recurse(i+1)

            if i < n-1 and 10 <= int(s[i:i+2]) <= 26:
                cache[i] += recurse(i+2)

            return cache[i]
        
        return recurse(0)
