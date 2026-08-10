"""
Features:
- Post tweet. Hashmap = tweets = {userId : ((ts,tweetId),(ts,tweetId2)..)} #timestamp is required
- Get tweet: Return the 10 most recent tweets of the user and the users the person is following.
- follow_unfollow relationship: Hashmap = {user: [following]}

{                          *
    sujit : [(1, pic1),(2,pic2), (8,pic3)]
                  *
    anthony : [(0,vid), (3, pic9)]
                     
    ritika : [(18, vid8)]
}

{
    sujit : (anthony, ritika, sujit)
}

BruteForce:
for user in sujit's following list: O((m*n) * nlogn) 
    feed = [all the posts]
    sort()
    return top 10

Optimal Approach:
max_heap = [(2,pic2),(0,vid) ] #(ts,post,idx,user)

(18,vid8), (8,pic3), (3,pic9)
TC: O(n * logn)

"""
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.followMap = defaultdict(set) #{user: [following]
        self.tweetMap = defaultdict(list) #{userId : ((ts,tweetId),(ts,tweetId2)..)}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweetMap[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        
        top10 = []
        maxHeap = []
        self.followMap[userId].add(userId)

        for user in self.followMap[userId]:
            if self.tweetMap[user]:
                idx = len(self.tweetMap[user]) - 1
                ts, tweet = self.tweetMap[user][idx]
                heapq.heappush(maxHeap, (-ts, tweet, user, idx-1))

        while maxHeap:

            ts, tweet, user, idx = heapq.heappop(maxHeap)
            top10.append(tweet)
                        
            if len(top10) == 10:
                return top10

            if idx >= 0:
                n_ts, n_tweet = self.tweetMap[user][idx]
                heapq.heappush(maxHeap, (-n_ts, n_tweet, user, idx-1))
        
        return top10
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        


































