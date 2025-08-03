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
            self.parent[py] = px
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_account = {}
        for i, account_entry in enumerate(accounts):
            emails = account_entry[1:]
            for email in emails:
                if email in email_to_account:
                    uf.union(email_to_account[email], i)
                else:
                    email_to_account[email] = i
        leader_to_emails = collections.defaultdict(list)
        for email, leader in email_to_account.items():
            leader_to_emails[uf.find(leader)].append(email)
        result = []
        for leader, emails in leader_to_emails.items():
            result.append([accounts[leader][0]] + sorted(emails))
        return result
        
        