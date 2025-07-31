class Twitter:
    def __init__(self):
        self.follow_map = collections.defaultdict(set)
        self.tweet_map = collections.defaultdict(collections.deque)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].appendleft((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow_map[userId].add(userId)
        max_heap = []
        for followeeId in self.follow_map[userId]:
            if self.tweet_map[followeeId]:
                time, tweetId = self.tweet_map[followeeId][0]
                max_heap.append((-time, tweetId, followeeId, 0))
        heapq.heapify(max_heap)
        result = []
        for _ in range(10):
            if not max_heap:
                break
            neg_time, tweetId, user, tweetIndex = heapq.heappop(max_heap)
            time = -neg_time
            result.append(tweetId)
            if tweetIndex + 1 < len(self.tweet_map[user]):
                time, next_tweet_id = self.tweet_map[user][tweetIndex + 1]
                heapq.heappush(max_heap, (-time, next_tweet_id, user, tweetIndex + 1))
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)