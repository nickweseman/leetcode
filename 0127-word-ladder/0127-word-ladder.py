class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        pattern_to_words = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_to_words[pattern].append(word)
        visited = set([beginWord])
        queue = collections.deque([beginWord])
        time = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return time
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in pattern_to_words[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            time += 1
        return 0
        
        
                