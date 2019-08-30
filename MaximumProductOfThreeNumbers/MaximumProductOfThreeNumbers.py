class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        res1 = nums[-1] * nums[-2] * nums[-3]
        res2 = nums[-1] * nums[0] * nums[1]

        res = max(res1, res2)
        return res


input = [1, 2, 3, 4]
assert Solution().maximumProduct(input) == 24
input = [1, 2, 3]
assert Solution().maximumProduct(input) == 6
input = [-4, -4, 2, 8]
assert Solution().maximumProduct(input) == 128

input = [-10, -9, -8, -7, 0, 1, 2, 3, 4, 5]
assert Solution().maximumProduct(input) == 450

input = [-10, -9, -8, -7]
assert Solution().maximumProduct(input) == -504
