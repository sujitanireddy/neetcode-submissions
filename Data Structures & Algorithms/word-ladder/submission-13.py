"""
early return case:
- if endWord not in wordList: return 0

{
    *at : [cat,bat]
    ba* : [bat,bag]
    *ag : [bag,sag]
}

"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
            
        wordList.append(beginWord)
        adjList = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adjList[pattern].append(word)

        q = deque()
        q.append(beginWord)
        visit = set()
        res = 1

        while q:

            for i in range(len(q)):

                word = q.popleft()

                if word == endWord:
                    return res

                visit.add(word)

                for i in range(len(word)):

                    pattern = word[:i] + '*' + word[i+1:]

                    for nei in adjList[pattern]:

                        if nei not in visit:
                            q.append(nei)

            res += 1
        
        return 0




