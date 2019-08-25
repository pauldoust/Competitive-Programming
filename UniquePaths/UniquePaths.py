class Solution:
    cached = None

    def traverseAll(self, i, j, m, n):
        if i < 0 or j < 0 or i >= n or j >= m:
            return 0
        if i == n - 1 and j == m - 1:
            return 1
        if self.cached[i][j] > 0:
            return self.cached[i][j]

        right = self.traverseAll(i, j + 1, m, n)
        down = self.traverseAll(i + 1, j, m, n)
        self.cached[i][j] = right + down
        return self.cached[i][j]

    def iterativeTraverseAll(self, m, n):
        if m == 0 and n == 0:
            return 0
        if m == 0 or n == 0:
            return 1
        for i in reversed(range(n)):
            for j in reversed((range(m))):
                if i == n - 1 and j == m - 1:
                    self.cached[i][j] = 1
                    continue
                else:
                    rightI = i
                    rightJ = j + 1
                    downI = i + 1
                    downJ = j
                    rightSol = 0
                    downSol = 0
                    if rightI >= 0 and rightI < n and rightJ >= 0 and rightJ < m:
                        rightSol += self.cached[rightI][rightJ]

                    if downI >= 0 and downI < n and downJ >= 0 and downJ < m:
                        downSol += self.cached[downI][downJ]

                    self.cached[i][j] = rightSol + downSol
        # print(self.cached)
        return self.cached[0][0]

    def uniquePaths(self, m: int, n: int) -> int:
        self.cached = [[0 for x in range(m)] for y in range(n)]
        # res = self.traverseAll(0, 0, m, n)
        res = self.iterativeTraverseAll(m, n)
        print("res: ", res)
        return res


assert Solution().uniquePaths(2, 2) == 2
assert Solution().uniquePaths(3, 2) == 3
assert Solution().uniquePaths(7, 3) == 28
assert Solution().uniquePaths(0, 0) == 0
assert Solution().uniquePaths(23, 12) == 193536720
assert Solution().uniquePaths(0, 3) == 1
