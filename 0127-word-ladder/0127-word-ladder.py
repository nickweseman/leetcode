class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        visited = set([beginWord])
        queue = collections.deque([beginWord])
        result = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei_word in nei[pattern]:
                        if nei_word not in visited:
                            queue.append(nei_word)
                            visited.add(nei_word)
            result += 1
        return 0