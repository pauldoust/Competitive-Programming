# https://leetcode.com/problems/non-decreasing-array/
# Runtime: 156 ms, faster than 98.33% of Python online submissions for Non-decreasing Array.
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastElement = None
        grace = 0
        problemPoint = None
        loopRange = range(0, len(nums))
        for i in loopRange:
            if lastElement is not None:
                if lastElement > nums[i]:
                    grace += 1
                    problemPoint = i
                    print('problem in: ', lastElement , " > ", nums[i])
                if grace > 1:
                    print('exceeded grace: ', grace)
                    return False
            lastElement = nums[i]

        if (problemPoint is None ) or (problemPoint == len(nums) -1) or problemPoint - 2 < 0:
            return True

        if nums[problemPoint - 1] <= nums[problemPoint + 1]:
            return True 

        if   nums[problemPoint - 2] <= nums[problemPoint ]:
            return True 


        return False


#  could be solved by brute force and shrinking the array to the smaller array with  important elements only
# inputList = [4,2,3]
# inputList = [2,3,3,2,4]
# inputList = [13, 4, 7]


# Fasles:
# inputList = [3,4,2,3]
# inputList = [4,2,1]
# inputList = [5,1,3,2,5] 
inputList = [12, 13, 4, 7]
new = inputList[:]
print(new)
i, j = 0, len(new) - 1
print (i, ' ' , j)
# print (Solution().checkPossibility(inputList))
