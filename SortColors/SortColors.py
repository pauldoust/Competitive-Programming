# https://leetcode.com/problems/sort-colors/
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(0,len(nums)):
        i = 0
        iterator = 0
        while iterator < len(nums):
            if nums[i] == 0:
                element = nums[i]
                nums.pop(i)
                nums.insert(0, element)
                # i += 1
            elif nums[i] == 2:
                element = nums[i]
                nums.pop(i)
                nums.append(element)
                i -= 1
            i += 1
            iterator += 1



# numList = [2, 2, 1, 0, 2, 1, 0]
# numList = [2,0,2,1,1,0]
numList = []
Solution().sortColors(numList)
print('**********')
print(numList)
# print (Solution().sortColors([3, 3, 2, 1, 3, 2, 1]))
 