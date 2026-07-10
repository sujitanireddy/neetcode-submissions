"""
- post tweets
- get top 10 recent tweets
- manage follow - unfollow relationship

DS:
user_tweet_map = {userid: [ts, tweetID]}
follow_map = {user: (users following)}

getnewsfeed:
- sorting. Combine all posts from all users the user is following - O(n * m) + O(nlogn) 
- max_heap = O(n * m), O(logn)     
- max_heap =  O(10 * logn)

"""
class Twitter:

    def __init__(self):
        self.user_tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ts += 1
        self.user_tweet_map[userId].append((self.ts, tweetId)) 

    def getNewsFeed(self, userId: int) -> List[int]:
        top10 = []
        self.follow_map[userId].add(userId)

        max_heap = [] #-ve values

        for user in self.follow_map[userId]:
            posts = self.user_tweet_map[user]
            if posts:
                ts, tweetId = posts[-1]
                idx = len(posts) - 1
                heapq.heappush(max_heap, (-ts, idx, tweetId, user))
        
        while max_heap and len(top10) < 10:
            ts, idx, tweetId, user = heapq.heappop(max_heap)
            top10.append(tweetId)
            idx -= 1
            
            if idx >= 0:
                ts, tweetId = self.user_tweet_map[user][idx]
                heapq.heappush(max_heap, (-ts, idx, tweetId, user))
        
        return top10

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        
