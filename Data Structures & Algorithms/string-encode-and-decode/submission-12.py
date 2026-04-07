class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '#'
        encoded_string = ''
        
        for word in strs:
            encoded_string += f'{len(word)}{delimiter}{word}'
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        delimiter = '#'
        decoded_list = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != delimiter:

                j += 1
            
            captured_length = s[i:j]

            start_of_word = j + 1
            end_of_word = start_of_word + int(captured_length)

            word = s[start_of_word:end_of_word]

            decoded_list.append(word)

            i = end_of_word
        
        return decoded_list




