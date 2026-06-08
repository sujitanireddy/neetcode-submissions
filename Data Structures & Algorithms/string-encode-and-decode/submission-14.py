class Solution:

    def encode(self, strs: List[str]) -> str:

        delimiter = '#'
        encoded_string = ""

        for s in strs:
            encoded_string += f"{len(s)}{delimiter}{s}"
        
        print(encoded_string)
        
        return encoded_string

    def decode(self, s: str) -> List[str]:

        delimiter = "#"
        decoded_string = []

        i = 0
        
        while i < len(s):

            j = i 

            while s[j] != delimiter:
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start: end]
            decoded_string.append(word)

            i = end
        
        return decoded_string





            