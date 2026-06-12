class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # userIds : followeeIds
        self.tweetMap = defaultdict(list) # userId : [(timestamp, tweetId)]
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweetMap[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        top10posts = []

        all_users = self.followMap[userId] | {userId}

        for user in all_users:
            posts = self.tweetMap[user]
            for timestamp, tweetId in posts:
                maxheap.append((-timestamp, tweetId))

        heapq.heapify(maxheap)
            
        while maxheap and len(top10posts) < 10:
            top10posts.append(heapq.heappop(maxheap)[1])
        
        return top10posts

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
