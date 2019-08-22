class Solution:
    def twoSum(self, nums, target: int) :
        firstRange = range(0,len(nums)-1) 
        for i in firstRange:
          for j in range(i+1, len(nums)):
              if nums[i] + nums[j] == target:
                  return [i, j]




# print(Solution().twoSum([1,2,3, 4, 5, 6], 3))
print(Solution().twoSum([-1,-2,-3,-4,-5], -8))
# print(Solution().twoSum([2, 7, 11, 15], 9))

