class Solution:
    def searchRange(self, nums, target: int) :
        if target in nums:
            start = nums.index(target)
            nums.reverse()
            end = nums.index(target)
            end = (len(nums) - end -1)
            result = [start , end]
            return result
        return [-1, -1]





# Test program 
# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
# x = 2
## [1, 4]

# arr = [5,7,7,8,8,10]
# x = 8
# #[3,4]

# arr = [5,7,7,8,8,10]
# x = 6

print(Solution().searchRange(arr, x))
