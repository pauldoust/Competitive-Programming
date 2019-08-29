class Solution:
    def moveZeroes(self, nums) -> None:
        i = 0
        numZeroes = 0
        while i < (len(nums) - numZeroes):
            if nums[i] == 0:
                val = nums.pop(i)
                nums.append(val)
                numZeroes += 1
            else:
                i += 1


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
assert nums == [1, 3, 12, 0, 0]

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeroes(nums)
assert nums == [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

nums = [1, 2, 3, 4, 10]
Solution().moveZeroes(nums)
assert nums == [1, 2, 3, 4, 10]

nums = []
Solution().moveZeroes(nums)
assert nums == []
