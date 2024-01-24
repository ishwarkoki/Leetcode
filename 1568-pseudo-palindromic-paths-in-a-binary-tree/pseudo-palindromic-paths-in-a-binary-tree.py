# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int: 

        # initialize the answer and the bit mask
        ans = 0
        mask = 0
        
        # define a helper function to traverse the tree
        def dfs(node):
            # use the nonlocal keyword to access the outer variables
            nonlocal ans, mask
            
            # base case: if the node is None, return
            if not node:
                return
            
            # update the bit mask by toggling the bit corresponding to the node value
            mask ^= (1 << node.val)
            
            # if the node is a leaf, check if the bit mask is pseudo-palindromic
            if not node.left and not node.right:
                # count the number of bits set to 1 in the bit mask
                # this can be done using Brian Kernighan's algorithm
                # see [Count set bits in an integer](https://leetcode.com/problemspseudo-palindromic-paths-in-a-binary-tree/?show=1) for more details
                count = 0
                n = mask
                while n:
                    n &= (n - 1)
                    count += 1
                
                # if the count is at most 1, the path is pseudo-palindromic
                if count <= 1:
                    ans += 1
            
            # otherwise, recursively traverse the left and right subtrees
            else:
                dfs(node.left)
                dfs(node.right)
            
            # backtrack by toggling the bit mask again
            mask ^= (1 << node.val)
        
        # call the helper function with the root node
        dfs(root)
        
        # return the answer
        return ans

        