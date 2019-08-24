class Solution:
    def pushDominoes(self, dominoes):
        currentMotion = None
        initiateDom = -1
        distances = [None] * len(dominoes)
        distanceFromInitiator = 200000
        resFirstIteration = ""
        for i in range(len(dominoes)):
            if initiateDom != -1:
                distanceFromInitiator = (i - initiateDom)
            dom = dominoes[i]
            if dom == "R":
                currentMotion = "R"
                initiateDom = i
                resFirstIteration += dom
            elif dom == "." and currentMotion == "R":

                resFirstIteration += 'R'
                distances[i] = distanceFromInitiator
            elif dom == "L":
                currentMotion = None
                resFirstIteration += dom
            else:
                resFirstIteration += dom

        currentMotion = None
        distanceFromInitiator = 200000
        resSecondIteration = ""
        initiateDom = -1
        for j in reversed(range(len(resFirstIteration))):
            if initiateDom != -1:
                distanceFromInitiator = (initiateDom - j)
            dom = resFirstIteration[j]
            if dom == "L":
                currentMotion = "L"
                initiateDom = j
                resSecondIteration += dom
            elif dom == "R" and distances[j] == None:
                resSecondIteration += dom
                currentMotion = None
            elif dom == "R" and distances[j] != None and distances[j] == distanceFromInitiator and currentMotion == "L":
                resSecondIteration += "."
                currentMotion = None
            elif dom == "R" and distances[j] != None and distances[j] > distanceFromInitiator and currentMotion == "L":
                resSecondIteration += "L"

            elif dom == "." and currentMotion == "L":
                resSecondIteration += "L"
            else:
                resSecondIteration += dom

        resSecondIteration = resSecondIteration[::-1]
        # print('resSecondIteration: ', resSecondIteration)
        return resSecondIteration


assert Solution().pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
assert Solution().pushDominoes("RR.L") == "RR.L"
assert Solution().pushDominoes("..R...L..R.") == "..RR.LL..RR"
assert Solution().pushDominoes(".........................") == "........................."
assert Solution().pushDominoes("........................L") == "LLLLLLLLLLLLLLLLLLLLLLLLL"
assert Solution().pushDominoes("R........................") == "RRRRRRRRRRRRRRRRRRRRRRRRR"
assert Solution().pushDominoes("R...L") == "RR.LL"
assert Solution().pushDominoes("R....L") == "RRRLLL"
assert Solution().pushDominoes("RLRLRL") == "RLRLRL"
assert Solution().pushDominoes("") == ""
assert Solution().pushDominoes("L") == "L"
assert Solution().pushDominoes("R") == "R"
assert Solution().pushDominoes("R..LLLLLL..........L") == "RRLLLLLLLLLLLLLLLLLL"
#

# Wrong Submission Cases
assert Solution().pushDominoes(
    "R..R..R.R..RR.RLR.LR.RRR.LLLLL.RR.RR...RR..RRRR..RR..R..RRRRRR...R.L..R..RRR.R...LRR..R..LRR.RR.RR.L") \
       == "RRRRRRRRRRRRRRRLR.LRRRRR.LLLLL.RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR.L..RRRRRRRRR.LLRRRRRRLLRRRRRRRR.L"
