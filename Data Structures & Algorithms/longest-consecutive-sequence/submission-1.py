class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        self.parent = {}
        self.rank = {}
        self.size = {}
        for num in nums:
            self.parent[num] = num
            self.rank[num] = 0
            self.size[num] = 1

        for num in nums:
            if num-1 not in self.parent:
                continue
            
            root_x, root_y = self.find(num-1), self.find(num)
            if root_x != root_y:
                self.union(root_x, root_y) 

        return max(self.size.values())
        

    def find(self, x: int) -> int:
        cur = self.parent[x]
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, x: int, y: int) -> None:
        sum_size = self.size[x] + self.size[y]
        self.size[x] = self.size[y] = sum_size
        print(sum_size)

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] += 1
