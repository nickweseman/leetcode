class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_to_accounts = {}
        for account_id in range(n):
            for email in accounts[account_id][1:]:
                if email in email_to_accounts:
                    uf.union(account_id, email_to_accounts[email])
                else:
                    email_to_accounts[email] = account_id
        leader_to_emails = collections.defaultdict(list)
        for email, account_id in email_to_accounts.items():
            leader = uf.find(account_id)
            leader_to_emails[leader].append(email)
        result = []
        for leader_id in leader_to_emails:
            name = accounts[leader_id][0]
            result.append([name] + sorted(leader_to_emails[leader_id]))
        return result
        
        