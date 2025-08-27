class Twitter:
    '''
    core logic of this problem lies in how we extract the feed for the user. 
    Adding and removing friends can simply be optimized using a set 

    Idea 1: 
    we keep a universal timestamp (this is common for idea 2 as well)
    Now, think about it this way: 
    for each user, we keep a list of their tweets along with a time stamp 

    When we need to retrieve a feed, we go ahead and merge all the tweet lists of the followers and the user itself and sort them in ascending order. We return the first 10. 
    This part will have a time complexity of log k * n 
    While doable this idea seems to be a bit more lengthy while coding. It is similar to merge k sorted lists on leetcode, good revision for that. 

    Idea 2: 
    A slightly more elegant solution in terms of implementation but might not be the prettiest when deploying for billions of people as storage would be a lot. 

    we store all the tweets with a time stamp in a priority q 
    so each users tweets are stored 
    userId -> user x tweet 1, user x tweet 2...
    while retriving the feed for a user, in this universal feed we match if the follower is in this feed and if yes, we pop it out. Since PQ as soon as we hit 10 we have an answer! 


    '''

    def __init__(self):
        self.timestamp = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # followed = self.following[userId] | {userId}
        # or simpley do 
        followed = set(self.following[userId])
        followed.add(userId)
        # cause here we are just adding the userId to make sure that we dont miss the user tweets 
        
        # Min-heap (using -timestamp for max-heap simulation)
        # python does not allow max heaps, so negative timestamp to make it a max heap 
        heap = []
        
        # Initialize heap with the latest tweet from each followed user (if any)
        for followeeId in followed:
            for t, tid in self.tweets[followeeId][-10:]:  # take last 10 tweets
                heapq.heappush(heap, (-t, tid))  # negate timestamp to simulate max-heap

    # Pop up to 10 most recent tweets
        feed = []
        for _ in range(min(10, len(heap))):
            feed.append(heapq.heappop(heap)[1])  # get tweet ID [1] has the tweetID [timestamp, tweetID]

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # cannot follow self
            self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)