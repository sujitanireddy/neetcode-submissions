#{user: [(ts, tweetId)]}
#{user: (following)}

class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        top_10 = []
        following = self.user_following[userId] | {userId}

        for user in following:
            posts = self.user_tweets[user]
            for ts, tweetId in posts:
                heapq.heappush(max_heap, (-ts, tweetId))
        
        heapq.heapify(max_heap)

        print(max_heap)

        while max_heap and len(top_10) < 10:
            ts, tweetId = heapq.heappop(max_heap)
            top_10.append(tweetId)
        
        return top_10
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)
        
