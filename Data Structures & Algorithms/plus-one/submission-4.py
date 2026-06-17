class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        collection = ""
        
        for num in digits:
            collection += str(num)
        
        collection = int(collection) + 1
        collection = str(collection)

        output = []
        for char in collection:
            output.append(int(char))
        
        return output
        

        