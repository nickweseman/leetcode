class Twitter:
    def __init__(self):
        self.time = 0
        self.follow_map = collections.defaultdict(set)
        self.user_tweets = collections.defaultdict(collections.deque)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].appendleft((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follow_map[userId]
        users.add(userId) # you get to see your own tweets without following yourself
        max_heap = []
        for user in users:
            if self.user_tweets[user]:
                timestamp, tweet_id = self.user_tweets[user][0]
                max_heap.append((-timestamp, tweet_id, user, 0))
        heapq.heapify(max_heap)
        result = []
        while max_heap and len(result) < 10:
            timestamp, tweet_id, user, tweet_idx = heapq.heappop(max_heap)
            result.append(tweet_id)
            if tweet_idx + 1 < len(self.user_tweets[user]):
                next_timestamp, next_tweet_id = self.user_tweets[user][tweet_idx + 1]
                heapq.heappush(max_heap, (-next_timestamp, next_tweet_id, user, tweet_idx + 1))
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)