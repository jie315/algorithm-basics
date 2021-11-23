# 二叉树
"""
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
"""

# 前序遍历：根左右

# 递归
def vlr(root):
  if not root: return []
  return [root.val] + vlr(root.left) + vlr(root.right)

# 循环
def vlr(root):
  stack = []
  result = []
  nd = root
  while len(stack) > 0 or nd != None:
    if nd:
      result.append(nd.val)
      stack.append(nd.right)
      nd = nd.left
    else:
      nd = stack.pop()
  return result
  
      
