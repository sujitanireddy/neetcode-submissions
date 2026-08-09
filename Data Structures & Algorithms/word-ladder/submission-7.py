class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        edgecase:
        - if endWord not in wordList: return 0

        cat -> bat -> bag -> sag
                       |
                      dag    dot

        BFS will always give us the shortet path from src to des

        AdjList { pattern: [words]} = {*at: [cat, bat ..]}

        - add begin word to the wordlist

        cat
        *at       
        c*t
        ca*
        """
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adjList = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adjList[pattern].append(word)

        print(adjList)
        
        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        res = 1

        while q:
            for i in range(len(q)):
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




        