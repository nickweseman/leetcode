class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. Build the graph. Using lists as stacks.
        # We sort the tickets in reverse to pop the lexicographically smallest
        # destinations first. pop() is an O(1) operation.
        adj = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        itinerary = []
        def dfs(airport):
            # 2. Greedily explore the path. As long as there's a destination,
            # keep going deeper.
            while adj[airport]:
                # Pop the next destination. Because of the reverse sort,
                # this is the lexicographically smallest one.
                next_destination = adj[airport].pop()
                dfs(next_destination)
            # 3. When you get stuck (the while loop condition is false),
            # it means this airport is the end of a path segment.
            # Add it to the itinerary.
            itinerary.append(airport)
        dfs("JFK")
        # 4. The itinerary was built backwards, so reverse it for the final answer.
        return itinerary[::-1]