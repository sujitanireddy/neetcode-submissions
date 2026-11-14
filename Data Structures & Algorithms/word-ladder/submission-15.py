"""
early return case:
if endWord is not in wordList:
    return 0


{
    *at : [cat, bat]
    c*t : [cat]
    ca* : [cat]
    b*t : [bat, bag]
    .
    .
}
TC: O(l * n)
SC: O(l * n)

where l is lenght of the words and n is length of wordlist

"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seq = 1
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adjList = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].append(word)
        
        q = deque()
        visit = set()
        q.append(beginWord)

        while q:

            for _ in range(len(q)):

                word = q.popleft()

                if word == endWord:
                    return seq

                visit.add(word)

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in adjList[pattern]:
                        if nei not in visit:
                            q.append(nei)
            seq += 1
        
        return 0























