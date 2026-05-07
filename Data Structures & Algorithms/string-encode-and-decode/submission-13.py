class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '#'
        encoded_string = ""

        for word in strs:
            encoded_string += f"{len(word)}{delimiter}{word}"

        return encoded_string

     #   5#Hello5#World
     #   i j



    def decode(self, s: str) -> List[str]:
        
        output = []
        delimiter = '#'
        i = 0

        while i < len(s):

            j = i

            while s[j] != delimiter:

                j += 1
            
            length = int(s[i:j])

            print(length)

            start_of_word = j + 1
            end_of_word = start_of_word + length
            word = s[start_of_word:end_of_word]

            output.append(word)

            i = end_of_word
        
        return output








