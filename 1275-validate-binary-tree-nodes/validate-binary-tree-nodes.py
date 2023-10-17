class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        inDegree = [0] * n
        root = -1

        # If inDegree of any node > 1, return False
        for child in leftChild:
            if child != -1:
                inDegree[child] += 1
                if inDegree[child] == 2:
                    return False

        for child in rightChild:
            if child != -1:
                inDegree[child] += 1
                if inDegree[child] == 2:
                    return False

        # Find the root (node with inDegree == 0)
        for i in range(n):
            if inDegree[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False  # Multiple roots

        # Didn't find the root
        if root == -1:
            return False

        return self.countNodes(root, leftChild, rightChild) == n

    def countNodes(self, root, leftChild, rightChild):
        if root == -1:
            return 0
        return 1 + \
            self.countNodes(leftChild[root], leftChild, rightChild) + \
            self.countNodes(rightChild[root], leftChild, rightChild)
