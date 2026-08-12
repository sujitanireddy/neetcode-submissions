class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = {char : set() for word in words for char in word}
        
        for i in range(len(words) - 1):
            
            curr_word = words[i]
            next_word = words[i+1]
            length = min(len(curr_word), len(next_word))

            if len(curr_word) > len(next_word) and curr_word[:length] == next_word: return ""

            for j in range(length):
                if curr_word[j] != next_word[j]:
                    adjList[curr_word[j]].add(next_word[j])
                    break
    
        
        visit = set()
        processed = set()
        res = []

        def dfs(char):

            if char in processed:
                return True
            
            if char in visit:
                return False
            
            visit.add(char)

            for nei in adjList[char]:
                if not dfs(nei):
                    return False
            
            res.append(char)
            processed.add(char)
            visit.remove(char)

            return True

        
        for char in adjList.keys():
            if not dfs(char):
                return ""
        
        final_res = "".join(res)

        return final_res[::-1]