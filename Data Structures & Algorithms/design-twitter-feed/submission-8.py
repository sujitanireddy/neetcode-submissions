class Twitter:

    #tweet_map = {userid: [(ts, tweetId)]}
    #follow_map = {userid: (followers)}

    def __init__(self): 
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.ts = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ts += 1
        self.tweet_map[userId].append((self.ts, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]: #TC: sorting: O(nlogn), max_heap: O(logn) 

        top10 = []

        max_heap = []

        self.follow_map[userId].add(userId)
        
        for follower in self.follow_map[userId]:

            for ts, tweetId in self.tweet_map[follower]:

                heapq.heappush(max_heap, (-ts, tweetId))

        while max_heap and len(top10) < 10:

            ts, tweetId = heapq.heappop(max_heap)
            
            top10.append(tweetId)

        return top10










    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
