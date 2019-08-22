class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:


    def addTwoNumbersRec(self, l1, l2, c = 0) -> ListNode:
        while l1 and l2:
            additionResult = (l1.val + l2.val + c )
            carry = int(additionResult / 10)
            additionResult = additionResult % 10
            result = ListNode(additionResult)
            l1 = l1.next
            l2 = l2.next
            if l1 == None and l2 == None and carry > 0:
                result.next = ListNode(carry)
                return result
            elif l1 == None and l2 != None:
                l1 = ListNode(0)
            elif l1 != None and l2 == None:
                l2 = ListNode(0)
            result.next = self.addTwoNumbersRec(l1, l2, carry)

            return result

    def addTwoNumbers(self, l1, l2) -> ListNode:
        carry = 0
        head = None
        while l1 and l2:
            additionResult = (l1.val + l2.val + carry )
            carry = int(additionResult / 10)
            additionResult = additionResult % 10
            newItem = ListNode(additionResult)
            if head == None:
                head = newItem
                curr = head
            else:
                curr.next = newItem
                curr = curr.next

            print('additionResult: ', additionResult)
            print('carry: ', carry)

            l1 = l1.next
            l2 = l2.next
            if l1 == None and l2 == None and carry > 0:
                print('case 1')
                l1 = ListNode(0)
                l2 = ListNode(0)
                # curr.next = ListNode(carry)
                # return curr
            elif l1 == None and l2 != None:
                print('case 2')
                l1 = ListNode(0)
            elif l1 != None and l2 == None:
                print('case 3')
                l2 = ListNode(0)

        return head


    def addTwoNumbersNumerical(self, l1, l2) -> ListNode:
        firstNumber = self.fromListToInteger(l1)
        secondNumber = self.fromListToInteger(l2)
        result = firstNumber + secondNumber
        return self.fromIntegerToList(result)

    def fromListToInteger(self, numlist):
        result = 0
        i = 0
        while numlist:
            result += numlist.val * (10** i)
            i += 1
            numlist = numlist.next
        return result




    def fromIntegerToList(self, numInteger):
        strNum = str(numInteger)
        resultListHead = ListNode(strNum[len(strNum)-1:])
        strNum = strNum[:len(strNum)-1]
        prev = resultListHead
        while strNum != "":
            resultList = ListNode(strNum[len(strNum)-1:])
            prev.next = resultList
            prev = resultList
            strNum = strNum[:len(strNum)-1]
            resultList = resultList.next

        return resultListHead




l1 = ListNode(1)

l2 = ListNode(9)
l2.next = ListNode(9)


result = Solution().addTwoNumbers(l1, l2)
print("-------------")
while result:
  print (result.val)    
  result = result.next
# 7 0 8

# 89 + 1 
#  + 1
