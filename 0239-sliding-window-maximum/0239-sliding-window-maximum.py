class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        left = right = 0
        result = []

        def add() -> None:
            while window and nums[window[-1]] < nums[right]:
                window.pop()
            window.append(right)
        def remove() -> None:
            if window[0] == left:
                window.popleft()
        
        while right < len(nums):
            add()

            if right - left + 1 > k:
                remove()
                left += 1
            if right - left + 1 == k:
                result.append(nums[window[0]])
            right += 1
        return result
        