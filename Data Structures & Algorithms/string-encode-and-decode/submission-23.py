"""
i             i
  j s         e
0 1 2 3 4 5 6 7 8 9 10 11 12 13
5 # H e l l o 5 # W o  r  l  d

len = 5
"""
class Solution:

    def encode(self, strs: List[str]) -> str:

        delimiter = "#"
        encoded_str = ""

        for word in strs:
            encoded_str += f"{len(word)}{delimiter}{word}"

        return encoded_str
        
    def decode(self, s: str) -> List[str]:

        print(s)

        #2#we3#say1#:3#yes10#!@#$%^&*()


        delimiter = "#"
        decoded_list = []
        i = 0 

        while i < len(s):

            j = i

            while s[j] != delimiter:
                j+=1

               
            length = s[i:j]

            start = j+1
            end = int(length) + start
            word = s[start:end]
            decoded_list.append(word)
            i = end
        
        return decoded_list



