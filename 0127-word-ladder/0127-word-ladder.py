class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        patterns = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        queue = collections.deque([beginWord])
        visited = {beginWord}
        time = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return time
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in patterns[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            time += 1
        return 0
