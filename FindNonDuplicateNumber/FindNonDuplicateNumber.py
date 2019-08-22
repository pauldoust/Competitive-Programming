# https://leetcode.com/problems/single-number/submissions/
# Runtime: 60 ms, faster than 97.63% of Python online submissions for Single Number.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listRange = range(0, len(nums))
        # print('nums: ', nums)
        xors = 0
        for i in listRange:
            xors ^= nums[i]
        return xors



# print( Solution().singleNumber([4, 3, 2, 4, 1, 3, 2]))
# print( Solution().singleNumber([4,1,2,1,2]))


# 4 100
# 1 001
# 2 010
# 1 001
# 2 010
#   ---
#   100