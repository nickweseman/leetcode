class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        left = right = 0
        result = []

        def add() -> None:
            while window and window[-1] < nums[right]:
                window.pop()
            window.append(nums[right])
        def remove() -> None:
            if window and nums[left] == window[0]:
                window.popleft()
        def validWindow() -> bool:
            return True
        def updateAnswer() -> None:
            result.append(window[0])
        while right < len(nums):
            add()
            if right - left + 1 > k:
                remove()
                left += 1
            if right - left + 1 == k and validWindow():
                updateAnswer()
            right += 1
        return result