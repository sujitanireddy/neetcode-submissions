class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        delimiter = '#'
        
        for s in strs:
            encoded_string += f'{len(s)}{delimiter}{s}'

        return encoded_string


    def decode(self, s: str) -> List[str]:

        decoded_list = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != '#':

                j += 1

            length_of_word = s[i:j]
            word_start_index = j + 1 
            word_end_index = word_start_index + int(length_of_word)

            word = s[word_start_index:word_end_index] 

            decoded_list.append(word)

            i = word_end_index
        

        return decoded_list






