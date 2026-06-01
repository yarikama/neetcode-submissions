class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        cur = self.par[x]
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
        elif self.rank[root_y] < self.rank[root_x]:
            self.par[root_x] = root_y
        else:
            self.par[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionFind = UnionFind(len(account))
        email_to_account_idx = {}

        for account_idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account_idx:
                    another_account_idx = email_to_account_idx[email]
                    unionFind.union(idx, another_account_idx)
                else:
                    email_to_account_idx[email] = account_idx

        return [[hello]]



    

