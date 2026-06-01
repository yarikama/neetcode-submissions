from heapq import heappop, heappush, nsmallest

class Twitter:

    def __init__(self):
        self.user_follows = defaultdict(set)
        self.user_posts = defaultdict(list)
        self.timeorder = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heappush(self.user_posts[userId], (-self.timeorder, tweetId))
        self.timeorder += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.user_follows[userId].add(userId)

        follow_num = {}
        pq = []
        for followee in self.user_follows[userId]:
            follow_num[followee] = 1
            time_stamp, lastest_post = nsmallest(1, self.user_posts[followee])[0]
            heappush(pq, (time_stamp, lastest_post, followee))

        if not pq:
            return []

        ans = []
        for i in range(10):
            if not pq:
                return ans
            _, post, followee = heappop(pq)
            ans.append(post)
            follow_num[followee] += 1
            if follow_num[followee] < len(self.user_posts[followee]):
                next_time_stamp, next_post = nsmallest(follow_num[followee], self.user_posts[followee])[follow_num[followee]]
                heappush(pq, (next_time_stamp, next_post, followee))

        return ans

        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].remove(followeeId)
        
