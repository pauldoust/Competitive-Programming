# Definition for singly-linked list.
class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        if head == None:
            return head
        # lastNth = head
        lastNth = None
        currentNode = head
        i = 0
        while currentNode:
            i += 1
            if i > (n):
                if lastNth == None:
                    lastNth = head
                else:
                    lastNth = lastNth.next
            currentNode = currentNode.next

        # print('lastNth.val: ', lastNth.val)
        if lastNth == None:
            head = head.next
        else:
            temp = lastNth.next
            lastNth.next = temp.next
            temp.next = None
        return head


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
head = Solution().removeNthFromEnd(head, 5)
print(head)

# head = Node(1, Node(2))
# print(head)
# head = Solution().removeNthFromEnd(head, 2)
# print(head)
