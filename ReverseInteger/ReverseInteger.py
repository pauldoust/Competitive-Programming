# https://leetcode.com/problems/reverse-integer/
# Runtime: 32 ms, faster than 96.20% of Python3 online submissions for Reverse Integer.
# Runtime: 36 ms, faster than 84.28% of Python3 online submissions for Reverse Integer.
# Runtime: 44 ms, faster than 22.92% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse1(self, x: int):
        if x >= 0:               
            strX = str(x)[::-1]
        else:
            strX = "-"+ str(x)[::-1][:-1]

        result = int(strX)
        bits = result.bit_length() 
        if bits > 31:
            result = 0

        return result

    def reverse2(self, x: int):
        if x >= 0:               
            strX = str(x)[::-1]
        else:
            # This modification increase the performance from 44ms to 36 ms 
            strX = "-" + str(- x)[::-1]

        result = int(strX)
        bits = result.bit_length() 
        if bits > 31:
            result = 0
  
  
    def reverse3(self, x: int):
        if x >= 0:               
            strX = str(x)[::-1]
        else:
            strX = "-" + str(- x)[::-1]

        result = int(strX)
  
        # This modification increase the performance from 36 ms to 32 ms
        if result in range(-2**31, 2**31 - 1  ):
            return result

        return 0



class Solution:
    def reverse(self, x: int):
        if x >= 0:               
            strX = str(x)[::-1]
        else:
            # This modification increase the performance from 44ms to 36 ms 
            strX = "-" + str(- x)[::-1]

        result = int(strX)
        # bits = result.bit_length() 
        # if bits > 31:
        #     result = 0
        if result in range(-2**31, 2**31 - 1  ):
            return result

        return 0



x = -1
# x = 1563847412

# print("s" , x.bit_length())
print ( Solution().reverse(x))
        