class Twitter:

    def __init__(self):
        self.follow_map = collections.defaultdict(set)
        self.tweet_map = collections.defaultdict(collections.deque)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].appendleft((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        news_followers = self.follow_map[userId].copy()
        news_followers.add(userId)
        for user in news_followers:
            if self.tweet_map[user]:
                time, tweet_id = self.tweet_map[user][0]
                max_heap.append((-time, user, tweet_id, 0))
        heapq.heapify(max_heap)
        result = []
        while max_heap and len(result) < 10:
            _, user, tweet_id, tweet_idx = heapq.heappop(max_heap)
            result.append(tweet_id)
            if tweet_idx + 1 < len(self.tweet_map[user]):
                time, tweet_id = self.tweet_map[user][tweet_idx + 1]
                heapq.heappush(max_heap, (-time, user, tweet_id, tweet_idx + 1))
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)