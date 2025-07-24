class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        left = right = 0
        result = []
        def add():
            while window and nums[window[-1]] < nums[right]:
                window.pop()
            window.append(right)
        def remove():
            if window[0] == left:
                window.popleft()
        def update_answer():
            result.append(nums[window[0]])
        while right < len(nums):
            add()
            if right - left + 1 > k:
                remove()
                left += 1
            if right - left + 1 == k:
                update_answer()
            right += 1
        return result