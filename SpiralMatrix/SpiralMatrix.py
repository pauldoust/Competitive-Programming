class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        result = []
        allElements = len(matrix) * len(matrix[0])
        scannedSoFar = 0
        currentI = 0
        currentJ = 0
        currentDirection = "R"
        level = 0
        # print('all: ', allElements)
        while scannedSoFar != allElements:
            # print('Direction: ', currentDirection, ", I: ", currentI, " j: ", currentJ)
            # print(matrix[currentI][currentJ])
            result.append((matrix[currentI][currentJ]))
            scannedSoFar += 1
            # print('scannedSoFar: ', scannedSoFar)
            if currentJ == (len(matrix[0]) - level - 1) and currentDirection == "R":
                currentDirection = "D"
            if currentI == (len(matrix) - level - 1) and currentDirection == "D":
                currentDirection = "L"
            if currentJ == level and currentDirection == "L":
                # print("go up")
                level += 1
                currentDirection = "U"
            if currentI == level and currentDirection == "U":
                currentDirection = "R"

            if currentDirection == "R":
                currentJ += 1
            if currentDirection == "D":
                currentI += 1
            if currentDirection == "L":
                currentJ -= 1
            if currentDirection == "U":
                currentI -= 1
        print(result)
        return result


#
mat = []
assert Solution().spiralOrder(mat) == []

mat = [
    [1],
    [5],
    [9]
]
assert Solution().spiralOrder(mat) == [1, 5, 9]

mat = [
    [1]
]
assert Solution().spiralOrder(mat) == [1]

mat = [
    [1, 2, 3, 4]
]
assert Solution().spiralOrder(mat) == [1, 2, 3, 4]

mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
assert Solution().spiralOrder(mat) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
assert Solution().spiralOrder(mat) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

mat = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]]

assert Solution().spiralOrder(mat) == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

mat = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]

assert Solution().spiralOrder(mat) == [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18,
                                       17, 12, 13]
