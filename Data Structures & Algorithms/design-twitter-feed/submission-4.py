class Twitter:

    def __init__(self):
        self.userPost = defaultdict(list)
        self.userFollow = defaultdict(set)
        self.ctr = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPost[userId].append((self.ctr, tweetId))
        self.ctr -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        self.userFollow[userId].add(userId)
        minHeap = []
        res = []

        for followee in self.userFollow[userId]:
            idx = len(self.userPost[followee]) - 1
            if idx >= 0:
                tweet = self.userPost[followee][idx]
                minHeap.append([tweet[0], tweet[1], followee, idx-1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            ctr, content, user, nextIdx = heapq.heappop(minHeap)
            res.append(content)

            if nextIdx >= 0:
                tweet = self.userPost[user][nextIdx]
                heapq.heappush(minHeap, [tweet[0], tweet[1], user, nextIdx-1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollow and followeeId in self.userFollow[followerId]:
            self.userFollow[followerId].remove(followeeId)