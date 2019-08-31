class Solution:
    def merge(self, intervals):
        intervals.sort()
        print('intervals: ', intervals)
        if len(intervals) == 0:
            return intervals
        if len(intervals) == 1 and (len(intervals[0]) == 0 or len(intervals[0]) == 1):
            return intervals
        result = []
        i = 0
        while i < len(intervals):
            current = intervals[i]
            if (i + 1 >= len(intervals)):
                result.append(current)
                break
            next = intervals[i + 1]
            extend = 0
            while next[0] >= current[0] and next[0] <= current[1]:
                current = [current[0], max(next[1], current[1])]
                if i >= len(intervals):
                    break
                extend += 1
                if i + extend + 1 >= len(intervals):
                    break
                next = intervals[i + extend + 1]

            result.append(current)
            if extend > 0:
                i += extend + 1
            else:
                i += 1
        print('result: ', result)
        return result

    # def merge(self, intervals):
    #     intervals.sort()
    #     if len(intervals) == 0:
    #         return  intervals
    #     if len(intervals) == 1 and len(intervals[0]) == 0:
    #         return  intervals
    #
    #     maxInterval = max([max (sublist) for sublist in intervals])
    #     maxInterval += 2
    #     nums = [False]*maxInterval
    #     result = []
    #     for interval in intervals:
    #         start = interval[0]
    #         end = interval[1]
    #         # print("start, end ", start, " ,", end)
    #         for i in range(start, end+1):
    #             print("i: ", i, "nums i ", nums[i], "nums i-1 ", nums[i-1] )
    #             if i == start and nums[i] == False and (nums[i-1] == True or nums[i-1] == "C"):
    #                 nums[i] = "C"
    #             else:
    #                 nums[i] = True
    #         print('nums: ', nums)
    #     rangeStarted = False
    #     item = []
    #     for i in range (0, len(nums)):
    #         if (nums[i] == True or nums[i] == "C") and rangeStarted == False:
    #             rangeStarted = True
    #             item.append(i)
    #         elif (nums[i] == False or nums[i] == "C") and rangeStarted:
    #             rangeStarted = False
    #             item.append(i-1)
    #             result.append(item)
    #             if nums[i] == "C":
    #                 item = [i]
    #                 rangeStarted = True
    #             else:
    #                 item = []
    #
    #     print('nums: ', nums)
    #     # print('result: ', result)
    #     return result


assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
assert Solution().merge([[1, 2]]) == [[1, 2]]
assert Solution().merge([[]]) == [[]]
assert Solution().merge([[1, 4], [5, 6]]) == [[1, 4], [5, 6]]
assert Solution().merge([[1, 4], [0, 4]]) == [[0, 4]]
assert Solution().merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
assert Solution().merge([[4, 5], [2, 4], [4, 6], [3, 4], [0, 0], [1, 1], [3, 5], [2, 2]]) == [[0, 0], [1, 1], [2, 6]]

assert Solution().merge([[1, 4], [2, 3]]) == [[1, 4]]
