class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for word in strs:

            freq_array = [0] * 26

            for letter in word:

                freq_array[ord(letter) - ord('a')] += 1

            anagrams[tuple(freq_array)].append(word)
        
        return list(anagrams.values())
        