class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  # Fill this in.

  print ("f: ", floor, " c: ", ceil)
  if root_node.left is None and  root_node.right is None:
  	if root_node.value > k:
  		return [None, None]
  	return [floor, ceil]

  if root_node.left is None:
  	return [root_node.value, root.right.value]

  if root_node.right is None:
  	return [root_node.left.value, root.value]


  if k <= root_node.value :
  	return findCeilingFloor(root_node.left, k, root_node.left.value, root_node.value)
  elif k > root_node.value :
  	return findCeilingFloor(root_node.right, k, root_node.value, root_node.right.value )
  # else:
  # 	# Equal
  # 	return [root_node.value, root_node.right.value]

# root = Node(8) 
# root.left = Node(4) 
# root.right = Node(12) 
  
# root.left.left = Node(2) 
# root.left.right = Node(6) 
  
# root.right.left = Node(10) 
# root.right.right = Node(14) 

root = Node(7) 
root.left = Node(5) 
root.right = Node(10) 
  
root.left.left = Node(3) 
root.left.right = Node(6) 
  
root.right.left = Node(8) 
root.right.right = Node(12) 

f = None
c = None
print ("---------------")
print(findCeilingFloor(root, 9, f, c))
# print ("f: ", f, " c: ", c)

#	 	 8
#  	   /   \
# 	  4     12
#   /  \   /   \
#  2   6  10   14