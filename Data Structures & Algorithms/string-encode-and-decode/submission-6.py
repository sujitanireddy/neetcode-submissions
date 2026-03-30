class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ''
        delimiter = '#'

        for i in range(len(strs)):

            length =  len(strs[i])

            encoded_string += f'{length}{delimiter}{strs[i]}'

        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_list = []
        delimiter = '#'
        i = 0
        
        while i < len(s):

            j = i

            while s[j] != delimiter:
                j+=1
            length = int(s[i:j])

            start = j+1
            end = start + length
            decoded_list.append(s[start:end])

            i = end
        
        return decoded_list
            




        

