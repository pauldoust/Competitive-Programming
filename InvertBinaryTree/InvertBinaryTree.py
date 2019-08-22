# https://leetcode.com/problems/invert-binary-tree/submissions/
# Runtime: 36 ms, faster than 73.12% of Python3 online submissions for Invert Binary Tree.

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.val = value

  def preorder(self):
    print (self.val)
    if self.left: self.left.preorder()
    if self.right: self.right.preorder()


class Solution:
    def invertTree(self, node):
        self.invert(node)
        return node

    def invert(self, node):
        if node == None:
            return
        temp = node.left
        node.left = node.right
        node.right = temp
        self.invertTree(node.left)
        self.invertTree(node.right)

# root = TreeNode('a') 
# root.left = TreeNode('b') 
# root.right = TreeNode('c') 
# root.left.left = TreeNode('d') 
# root.left.right = TreeNode('e') 
# root.right.left = TreeNode('f') 

root = TreeNode(4) 
root.left = TreeNode(2) 
root.right = TreeNode(7) 
root.left.left = TreeNode(1) 
root.left.right = TreeNode(3) 
root.right.left = TreeNode(6) 
root.right.right = TreeNode(9) 


root.preorder()
# a b d e c f 
print ("\n")
f = Solution().invertTree(root)
f.preorder()
# a c f b e d