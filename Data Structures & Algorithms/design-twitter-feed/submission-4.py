class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list) #{userid : [(timestamp, tweetId)]}
        self.user_following = defaultdict(set) #{userid : (following list)}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.user_tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        top10 = []
        maxheap = []
        all_following = self.user_following[userId] | {userId}

        for user in all_following:
            for ts, tweetId in self.user_tweets[user]:
                heapq.heappush(maxheap, (-ts, tweetId))
        
        heapq.heapify(maxheap)

        while maxheap and len(top10) < 10:
            tweetId = heapq.heappop(maxheap)[1]
            top10.append(tweetId)

        return top10

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)