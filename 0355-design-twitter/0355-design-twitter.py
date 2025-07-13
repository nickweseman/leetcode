class Twitter:
    def __init__(self):
        self.follower_map = collections.defaultdict(set)
        self.tweet_map = collections.defaultdict(collections.deque)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].appendleft((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        fset = self.follower_map[userId].copy()
        fset.add(userId)
        max_heap = []
        for followee in fset:
            if self.tweet_map[followee]:
                timestamp, tweet_id = self.tweet_map[followee][0]
                heapq.heappush(max_heap, (-timestamp, tweet_id, followee, 0))
        result = []
        while max_heap and len(result) < 10:
            neg_timestamp, tweet_id, user_id, i = heapq.heappop(max_heap)
            timestamp = -neg_timestamp
            result.append(tweet_id)
            if i + 1 < len(self.tweet_map[user_id]):
                next_timestamp, next_tweet_id = self.tweet_map[user_id][i + 1]
                heapq.heappush(max_heap, (-next_timestamp, next_tweet_id, user_id, i + 1))   
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)