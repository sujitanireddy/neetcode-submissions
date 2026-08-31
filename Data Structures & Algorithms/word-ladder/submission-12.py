"""
cat -> sag
cat -> bat -> bag -> sag
["bat","bag","sag","dag","dot"]

edgecase:
- if endWord not in wordList: return 0

patters:
*at
c*t
ca*

{
    *at : [cat,bat]
    c*t : [cat]
    ca* : [cat]
    *ag :
}

TC: (m * n)
SC: (m * n)
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        adjList = defaultdict(list)
        wordList.append(beginWord)
        if endWord not in wordList: return 0

        for word in wordList:
            for j in range(len(beginWord)):
                pattern = word[:j] + '*' + word[j+1:]
                adjList[pattern].append(word)
        
        visit = set()
        visit.add(beginWord)
        res = 1
        q = deque()
        q.append(beginWord)

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(beginWord)):
                    pattern = word[:j] + '*' + word[j+1:]
                    
                    for nei in adjList[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            
            res += 1


        return 0
































