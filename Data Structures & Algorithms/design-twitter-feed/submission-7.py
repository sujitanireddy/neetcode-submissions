#{user: [(ts, tweetId)]}
#{user: (following)}

class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        top_10 = []
        self.user_following[userId].add(userId)

        for user in self.user_following[userId]:
            if user in self.user_tweets:
                index = len(self.user_tweets[user]) - 1
                ts, tweetId = self.user_tweets[user][index]
                heapq.heappush(max_heap, (ts, tweetId, user, index - 1))

        while max_heap and len(top_10) < 10:
            ts, tweetId, user, index = heapq.heappop(max_heap)
            top_10.append(tweetId)

            if index >= 0:
                ts, tweetId = self.user_tweets[user][index]
                heapq.heappush(max_heap, (ts, tweetId, user, index - 1))
        
        return top_10
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)
        
