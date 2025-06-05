# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = previous = None

        def inorder(node):
            nonlocal first, second, previous
            if not node:
                return

            inorder(node.left)

            if previous and previous.val > node.val:
                if not first:
                    first = previous
                second = node
            previous = node

            inorder(node.right)

        inorder(root)

        if first and second:
            swapper = first.val
            first.val = second.val
            second.val = swapper
