# https://leetcode.com/problems/string-to-integer-atoi/
# Runtime: 40 ms, faster than 74.58% of Python3 online submissions for String to Integer (atoi).
class Solution:
    def isNumber(self, s):
        try:
            float(s)
        except ValueError:
            return False
        return True

    def myAtoi(self, s) :
        INT_MIN , INT_MAX = -2**31,  (2**31) -1
        allowedRange = range(INT_MIN, INT_MAX)
        f = [st for st in s.split() ]
        # print(f)
        if len(f) > 0:               
            firstNumber = f[0]
            numericalPart = ""
            for character in firstNumber:
                if character.isdigit() or character == "+" or character == "-" :
                    if self.isNumber(numericalPart) and not character.isdigit():
                        break
                    numericalPart  += character
                else:
                    break
            if numericalPart == "" or not self.isNumber(numericalPart):
                return 0
            firstNumber = int(numericalPart)
            if firstNumber in allowedRange:
                return firstNumber

            result = INT_MAX if firstNumber >= INT_MAX else INT_MIN
            return result

        return 0

# s = "  -0012a42"
# s = ".1"
# s = "3.14159"
s = "+11e530408314"
s = ""
s = "42"
s = "   -42"
s = "    4193 with words"
s = "words and 987"
s = "-91283472332"
s = "+1"
s = "2147483647"
s = "-5-"
# s = "-13+8"
print( Solution().myAtoi(s))
