class Solution:
	def matched(self, firstCharacter, secondCharacter):
		if firstCharacter == '(':
			return secondCharacter == ')'

		if firstCharacter == '[':
			return secondCharacter == ']'
			
		if firstCharacter == '{':
			return secondCharacter == '}'

	def isValid(self, s):
		if s =="":
			return True
		headofStack = ""
		stack = []
		for character in s:
			# print("head of stack: ", headofStack)
			# print("character: ", character)
			# print("stack: ", stack)
			if self.matched(headofStack, character):
				# print("matched !, pop")
				stack.pop()
				if len(stack) == 0:
					headofStack = ""
				else:
					headofStack = stack[-1]
			else:
				# print("not matched !, push")
				headofStack = character
				stack.append(character)
		# print('final stack: ', stack)
		return len(stack) == 0

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))




s = "((()))"
# should return True
print(Solution().isValid(s))


s = "[()]{}"
# should return True
print(Solution().isValid(s))


s = "({[)]"
# should return True
print(Solution().isValid(s))

print("****************")


s = "()"
# should return True
print(Solution().isValid(s))




s = "()[]{}"
# should return True
print(Solution().isValid(s))



s = "(]"
# should return True
print(Solution().isValid(s))



s = "([)]"
# should return True
print(Solution().isValid(s))



s = "{[]}"
# should return True
print(Solution().isValid(s))
