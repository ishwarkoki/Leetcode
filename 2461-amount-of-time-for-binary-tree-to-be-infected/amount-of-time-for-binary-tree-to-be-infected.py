# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int: 
        parentMap = {root.val : None} ; visited = set() ; q = deque()


        # build the parent child unordered hashmap  
        def dfs(node): 

            if not node : 
                return 

            if node.left : 
                parentMap[node.left.val] = node 

            if node.right : 
                parentMap[node.right.val] = node 

            dfs(node.left) 
            dfs(node.right) 

        dfs(root)  

        # Do a BFS (level order Traversal) with modification : exploring childs && parent aswell. 

        def bfs(target) : 
            
            q.append(target)
            visited.add(target) 
            level = 0

            while q : 

                length = len(q)
                for _ in range(length): 

                    curNode = q.popleft() 
                    if curNode.left and curNode.left not in visited : 
                        q.append(curNode.left)
                        visited.add(curNode.left)

                    if parentMap[curNode.val] and parentMap[curNode.val] not in visited : 
                        q.append(parentMap[curNode.val]) 
                        visited.add(parentMap[curNode.val])  

                    if curNode.right and curNode.right not in visited : 
                        q.append(curNode.right) 
                        visited.add(curNode.right)  

                level+=1  

            return level-1

        def travel(node): 
            if not node: 
                return 

            if node.val == start: 
                return node
 
            return travel(node.left) or travel(node.right) 
            

        startNode = travel(root) 
        ans = bfs(startNode)          
        return ans 