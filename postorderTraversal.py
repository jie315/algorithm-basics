# 二叉树
"""
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
"""

# 后序遍历：左右根

# 递归
def lrd(root):
  if not root: return []
  return lrd(root.left) + lrd(root.right) + [root.val]

# 循环
# 根右左 -> 取反
def lrd(root):
  stack = []
  result = []
  nd = root
  while len(stack) > 0 or nd != None:
    if nd:
      result.append(nd.val)
      stack.append(nd.left)
      nd = nd.right
    else:
      nd = stack.pop()
  return result[::-1]
  
