class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = collections.Counter()
        target = collections.Counter(s1)
        left = right = 0
        have = 0
        need = len(target)

        while right < len(s2):
            window[s2[right]] += 1
            if window[s2[right]] == target[s2[right]]:
                #print("HAAAAAAAAAAAAAAVE")
                have += 1

            if right - left + 1 > len(s1):
                #print(f"entering if loop what was {right=} {left=}")
                if window[s2[left]] == target[s2[left]]:
                    have -= 1
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            #print(locals())
            if right - left + 1 == len(s1) and have == need:
                return True
            right += 1
        return False