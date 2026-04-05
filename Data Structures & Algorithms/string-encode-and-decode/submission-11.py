class Solution:

    def encode(self, strs: List[str]) -> str:

        delimiter = '#'
        encoded_string = ''

        for word in strs:
            encoded_string += f'{len(word)}{delimiter}{word}'
        
        return encoded_string

    def decode(self, s: str) -> List[str]:

        delimiter = '#'
        strs = []
        i = 0

        while i < len(s):

            j = i
            
            while s[j] != delimiter:

                j += 1
            
            length_captured = int(s[i:j])

            start_of_word = j + 1
            end_of_word = start_of_word + length_captured

            word = s[start_of_word:end_of_word]

            strs.append(word)

            i = end_of_word
        
        return strs




