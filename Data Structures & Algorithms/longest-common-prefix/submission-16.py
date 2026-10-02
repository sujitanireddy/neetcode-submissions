"""
  0 1   2   3
  b a   t
  b a   g
  b a   n   k
  b a   n   d


l = len of a the smallest word

TC: O(n * l)
SC: O(1)

Pseudocode:

min_length = float("inf")
res = ''

for word in strs:
    min_length = min(min_length, len(word))

for i in range(min_length):

    char = strs[0][i]

    for word in strs:

        if char != word[i]:
            return res

    res += char

return res

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")

        res = ""

        for word in strs:
            min_length = min(min_length, len(word))

        for i in range(min_length):
            char = strs[0][i]

            for word in strs:
                if char != word[i]:
                    return res

            res += char

        return res
