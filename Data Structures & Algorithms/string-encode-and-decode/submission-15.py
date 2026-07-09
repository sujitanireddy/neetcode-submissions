class Solution:

    """                 ij
    ["Hello","World"] = 5#Hello5#World
    encode = len(s) + delimiter + string
    
    5#Hello5#World


    decode
    - until we hit the delimiter it's the length. 
    - From delimiter capture the word using length
    - Jump to end of the word

    """
    #TC: O(n)
    #SC: O(n)
    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}{delimiter}{s}"
        return encoded_string

    #TC: O(n)
    #SC: O(n)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        delimiter = "#"
        i = 0
        while i < len(s):
            j = i
            while s[j] != delimiter:
                j += 1
            length = s[i:j]
            start = j+1
            end = start + int(length)
            word = s[start:end]
            decoded_strs.append(word)
            i = end
        return decoded_strs

            


