class Solution:
    graph = {}
    visited = None

    def constructGraph(self, numCourses, prerequisites):
        for pair in prerequisites:
            if not pair[0] in self.graph.keys():
                self.graph[pair[0]] = [pair[1]]
            else:
                self.graph[pair[0]].append(pair[1])
        # print('self.graph: ', self.graph)
        self.visited = [False] * numCourses

    def findCycles(self, root, numCourses):
        # print("root: ", root, " visited: ", self.visited)
        if self.visited[root] == "Done":
            return True
        if self.visited[root]:
            return False
        self.visited[root] = True
        if not (root in self.graph.keys()):
            self.visited[root] = "Done"
            return True
            # if sum(self.visited) == numCourses:
            #     return True
            # else:
            #     return False
        for neighbour in self.graph[root]:
            result = self.findCycles(neighbour, numCourses)
            if not result:
                return False
        self.visited[root] = "Done"
        return True

    def canFinish(self, numCourses, prerequisites) -> bool:
        self.graph = {}
        self.visited = None
        if numCourses == 0:
            return True
        if len(prerequisites) == 0:
            return True

        self.constructGraph(numCourses, prerequisites)
        # print (self.visited)
        # print (sum(self.visited))
        for preq in prerequisites:
            if not self.findCycles(preq[0], numCourses):
                return False
        return True


assert Solution().canFinish(2, [[1, 0]]) == True
assert Solution().canFinish(2, [[1, 0], [0, 1]]) == False
assert Solution().canFinish(2, []) == True
assert Solution().canFinish(2, [[0, 1]]) == True
assert Solution().canFinish(3, [[1, 0]]) == True

assert Solution().canFinish(3, [[0, 1], [0, 2], [1, 2]]) == True

assert Solution().canFinish(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]) == False
