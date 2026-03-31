class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #for every word in strs build a freq tuple and add it to 
        #dict with the tuple as key and the words as values. Return
        #the values at the end in the form of lists

        same_anagrams = defaultdict(list)

        for word in strs:

            freq_array = [0] * 26

            for char in word:
            
                freq_array[ord(char) - ord('a')] += 1

            same_anagrams[tuple(freq_array)].append(word)
        
        return list(same_anagrams.values())
        