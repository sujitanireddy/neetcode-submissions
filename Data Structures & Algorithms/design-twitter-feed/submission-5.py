"""
What are the functionlities required and what are the constrains?

functionlities
- Post a tweet
- Fetch latest 10 new tweets of (themselves + people following)
- Follow and unfollow relationship

constraints
- Posts should be ordered from most recent to least recent (keep track of time or some metric which uniquly tells us the order of posts)
- When we do a get, posts should be the last 10 based on the above metric

Implementation detials:

- hashmap: (user_tweets_map) {userId: [(tweetId1, timestamp)]} #timestamp is a member variable which is global and will be incrementing everything post is called
- hashmap: (user_following_map) {followerId : (followeeId's)} #who are all the people the person is following
- list: top10 and max_heap:  

"""
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweets_map = defaultdict(list) #{userId: [(timestamp, tweetId1)]}
        self.user_following_map = defaultdict(set) #{userId : (followeeId's)}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.user_tweets_map[userId].append((self.timestamp, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        top10 = []
        following = {userId} | self.user_following_map[userId]
        max_heap = []

        for user in following:
            for timestamp, tweetId in self.user_tweets_map[user]:
                max_heap.append((-timestamp, tweetId))
        
        heapq.heapify(max_heap)

        while max_heap and len(top10) < 10:
            timestamp, tweetId = heapq.heappop(max_heap)
            top10.append(tweetId)
        
        return top10

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following_map[followerId]:
            self.user_following_map[followerId].remove(followeeId)
