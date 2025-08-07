class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort(reverse=True)
        for a, b in tickets:
            adj[a].append(b)
        result = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            result.append(src)
        dfs("JFK")
        return result[::-1]
