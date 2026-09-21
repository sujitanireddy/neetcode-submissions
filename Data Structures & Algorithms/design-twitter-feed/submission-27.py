"""
Features:
- Post tweets
- Follow - Unfollow
- View 10 most recent tweets

tweet_map:

{
    userId : [tweetId,tweetIds..]
}

{
    1 : [(ts,10)]
    2 : [20,30,40,50,60]
}

follow_map: 

{
    user : (following)
}

{
    1 : 2
}

O(nlogm * n)


{                       
    1 : [(1,1),(6,9),(9,100)]
    
    2 : [(2,900),(20,7),(30,1)]

    3 : [(8,88)]
}

max_heap = [(9,100), (8,88), (2,900) ]

1,20,10...

mlogn
"""
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweet_map[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        
        top10 = []
        maxHeap = []

        self.follow_map[userId].add(userId)

        for user in self.follow_map[userId]:
            if self.tweet_map[user]:
                idx = len(self.tweet_map[user]) - 1
                ts, tweetId = self.tweet_map[user][idx]
                heapq.heappush(maxHeap, (-ts, tweetId, user, idx))

        while maxHeap and len(top10) < 10:
            ts, tweetId, user, idx = heapq.heappop(maxHeap)
            top10.append(tweetId)

            if idx > 0:
                ts, tweetId = self.tweet_map[user][idx - 1]
                heapq.heappush(maxHeap, (-ts, tweetId, user, idx - 1))

        return top10

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        
