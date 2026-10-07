"""
["hrn","hrf","er","enn","rfnn"]

enn rfnn

n -> f
h -> e
r -> n
e -> r

hernf
{
    n : [f]
    h : [e]
    r : [n]
    e : [r]
}

- Build adjList
- Topological Sort
- return reverse of the ans
"""
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = {char : [] for word in words for char in word}

        for i in range(1, len(words)):
            word_A = words[i-1]
            word_B = words[i]
            first_length = len(word_A)
            second_length = len(word_B)
            length = min(first_length, second_length)
            
            #prefix check
            if first_length > second_length:
                if word_A[:second_length] == word_B:
                    return ""

            for j in range(length):
                if word_A[j] != word_B[j]:
                    adjList[word_A[j]].append(word_B[j])
                    break
        
        
        #topological sort
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
            visit.remove(char)
            processed.add(char)

            return True


        for key in adjList.keys():
            if key not in processed:
                if not dfs(key):
                    return ""

        return "".join(res)[::-1]




