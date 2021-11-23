# 二叉树
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# 层序遍历（逐层，从左往右遍历节点）
def levelTraversal(root):
  if not root: return []
  result = []
  queue = [root]
  while len(queue) > 0:
    nd = queue.pop(0)
    result.append(nd.val)
    if nd.left:
      queue.append(nd.left)
    if nd.right:
      queue.append(nd.right)
  return result
