"""
Notes:
- 1 char diff
- If endWord not in wordList: return 0
- append beingWord to wordList before builing the adjList

"cat" -> "bat" -> "bag" -> "sag"

Shortest Path (BFS)
- Graph rep: AdjList

{   
    cat : [bat]
    bat : [bag]
    bag : [sag, dag]
    dag : []
    dot : []
}

pattern: 
{   
    *at : [cat, bat]
    c*t : [cat]
    ca* : [cat]
    b*t : [bat]
    ba* : [bat]
    *ag : [sag, dag]
}

len word = m
len wordList = n

TC to build AdjList : O(n * m)
BFS : O(V+E)

TC: O(n*m + V+E)
SC: O(m*n)

3

[bat]

"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList: return 0
        
        wordList.append(beginWord)
        adjList = defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adjList[pattern].add(word)

        q = deque()
        q.append(beginWord)
        counter = 1
        visit = set()
        visit.add(beginWord)

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return counter

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in adjList[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
                
            counter += 1
        
        return 0



"""
[]



"""
































