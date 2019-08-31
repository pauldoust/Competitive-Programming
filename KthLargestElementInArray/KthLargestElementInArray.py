class Solution:
    def findKthLargest(self, nums, k: int):
        nums.sort(reverse=True)
        return nums[k - 1]


assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert Solution().findKthLargest([3, 5, 2, 4, 6, 8], 3) == 5
assert Solution().findKthLargest([3], 1) == 3
