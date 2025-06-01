class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i, j = len(players) - 1, len(trainers) - 1
        matchings = 0
        
        players.sort()
        trainers.sort()
        
        while i >= 0 and j >= 0:
            if players[i] <= trainers[j]:
                j -= 1
                matchings += 1
            i -= 1
        return matchings

        