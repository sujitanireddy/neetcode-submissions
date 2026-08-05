class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        #Build adjList with patterns as keys and words as neighbours
        adjList = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adjList[pattern].append(word)
            
        q = deque()
        visit = set()
        visit.add(beginWord)
        q.append(beginWord)
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adjList[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            
            res += 1
        
        return 0
        

