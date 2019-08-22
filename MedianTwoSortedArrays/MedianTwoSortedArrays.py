# # https://leetcode.com/problems/median-of-two-sorted-arrays/
# Runtime: 68 ms, faster than 94.33% of Python online submissions for Median of Two Sorted Arrays.
# Memory Usage: 11.8 MB, less than 93.62% of Python online submissions for Median of Two Sorted Arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = list(nums1 + nums2)
        merged.sort()
        halfIndex = int(len(merged) /2)
        if len(merged) % 2 == 0:
        	return float((merged[halfIndex] + merged[halfIndex -1])/2.0)

        return float(merged[halfIndex])