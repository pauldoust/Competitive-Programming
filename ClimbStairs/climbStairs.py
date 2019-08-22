# Runtime: 32 ms, faster than 89.06% of Python3 online submissions for Climbing Stairs.
class Solution:
    def climbStairs(self, n: int) -> int:
        numberOfWays = [None] * (n+1)
        numberOfWays[0] = 1
        numberOfWays[1] = 1
        
        stairsRange = range(2, n+1)

        for i in stairsRange:
        	numberOfWays[i] = numberOfWays[i-1] + numberOfWays[i-2]

        return numberOfWays[n]


    def climbStairsMemoryEfficient(self, n: int) -> int:
        numberOfWaysPrevious = 1
        numberOfWaysSecondPrevious = 1 
        currentNumberOfWays = 1
        stairsRange = range(2, n+1)
        for i in stairsRange:
        	currentNumberOfWays = numberOfWaysPrevious + numberOfWaysSecondPrevious
        	numberOfWaysSecondPrevious = numberOfWaysPrevious
        	numberOfWaysPrevious = currentNumberOfWays

        return currentNumberOfWays


print(Solution().climbStairs(2))
