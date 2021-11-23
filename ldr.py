# 二叉树
"""
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
"""

# 前序遍历：左根右

# 递归
def ldr(root):
  if not root: return []
  return vlr(root.left) + [root.val] + vlr(root.right)

# 循环
def vlr(root):
  stack = []
  result = []
  nd = root
  while len(stack) > 0 or nd != None:
    if nd:
      stack.append(nd)
      nd = nd.left
    else:
      nd = stack.pop()
      result.append(nd.val)
      nd = nd.right
  return result
