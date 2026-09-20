"""
["Hello","World"]
5#hello5#World
"""
class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        delimiter = "#"

        for word in strs:
            encoded_string += f"{len(word)}{delimiter}{word}"
        
        return encoded_string
    # 01234567
    # i
    #  j     i 
    # 5#hello5#World
    def decode(self, s: str) -> List[str]:

        delimiter = "#"
        decoded_list = []
        i = 0

        while i < len(s):

            j = i

            while s[j] != delimiter:
                j += 1
            
            length = int(s[i:j])

            start = j + 1
            end = start + length
            word = s[start:end]
            decoded_list.append(word)

            i = end

        return decoded_list



