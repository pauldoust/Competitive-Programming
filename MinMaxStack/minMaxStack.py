# https://leetcode.com/problems/min-stack/submissions/
# Runtime: 72 ms, faster than 73.80% of Python3 online submissions for Min Stack.
# Runtime: 68 ms, faster than 89.48% of Python3 online submissions for Min Stack.
class MinStack:
    stack = []
    minElement = None
    # minElement = 2**32-1

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        if self.minElement == None or  x <= self.minElement:
            self.stack.append("prevMin:" + str(self.minElement))
            self.minElement = x
        self.stack.append(x)


    def pop(self):
        topElement = self.top() 
        self.stack.pop()
        if  topElement == self.minElement:
            if len(self.stack) > 0:
                elem = self.stack.pop().split(":")[1]
                if elem == None or elem == "None":
                    self.minElement = None
                else:
                    self.minElement  = int(elem)
            else:
                self.minElement = None
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.minElement


# # Your MinStack object will be instantiated and called as such:
# x = 5
# obj = MinStack()
# obj.push(x)
# obj.push(3)
# print(obj.pop())
# param_3 = obj.top()
# param_4 = obj.getMin()

# print("top: ", param_3)
# print("min: ", param_4)


# minStack = MinStack()
# minStack.push(512)
# minStack.push(-1024)
# minStack.push(-1024)
# minStack.push(512)
# minStack.pop()
# print(minStack.getMin())
# minStack.pop()
# print(minStack.getMin())
# minStack.pop()
# print(minStack.getMin())


# elem =  None

# print('elem: ', elem)
# print('elem: ', elem)