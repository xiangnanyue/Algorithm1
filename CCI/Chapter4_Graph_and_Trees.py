
#4.1 route between Nodes
#

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution4_1:
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """

    def hasRoute(self, graph, s, t):
        # write your code here
        if s.label == t.label:
            return True
        visited = {}
        stack = []
        
        stack.append(s)
        visited[s.label] = True
        
        while len(stack) > 0:
            visitingnode = stack.pop()
            for n in visitingnode.neighbors:
                if n.label == t.label:
                    return True
                if visited.get(n.label) is None:
                    stack.append(n)
                    visited[n.label] = True
                
        return False


#4.2 minimal tree
#
#

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution4_2:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        # balanced BST ?
        length = len(A)
        if length == 0:
            return None
        
        mid = int(length/2) if length%2==1 else int(length/2)-1
        node = TreeNode(A[mid])
        node.left = self.sortedArrayToBST(A[:mid])
        node.right = self.sortedArrayToBST(A[mid+1:])
        
        return node


#
#4.3 List of Depths
#


#
#4.4 check balance
#https://www.lintcode.com/problem/balanced-binary-tree/description
# is there a non-recursive method ?
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution4_4:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        isleftbalance

    def balanceDepth_(self, node):
        if node is None:
            return True, 0
        isleftbalance, leftDepth = self.balanceDepth_(node.left)
        isrightbalance, rightDepth = self.balanceDepth_(node.right)
        return isleftbalance and isrightbalance and abs(leftDepth-rightDepth)<2, max(leftDepth, rightDepth)+1
#
#4.5 validate BST
#https://www.lintcode.com/problem/validate-binary-search-tree/description

    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST4_5(self, root):
        # use a global variable for recursive reason
        self.leftlast = float("-inf")
        return self.helper_(root)
        
    def helper_(self, root):
        if root is None:
            return True
        if not self.helper_(root.left):
            return False
        if root.val <= self.leftlast:
            return False
        self.leftlast = root.val
        if not self.helper_(root.right):
            return False
        return True

#
#exercise: use BST to solve wood cut problem
#https://www.lintcode.com/problem/wood-cut/description

class WoodCut:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        pass


#
#4.6 in order successor
#https://www.lintcode.com/problem/inorder-successor-in-bst/description

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution4_6:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        # we used a global variable self.head
        head = TreeNode(None)
        self.head = head
        self.getLinkedList(root)
        while head.right is not None:
            if head.right.val == p.val:
                return head.right.right
            else:
                head = head.right
        return None
        
    def getLinkedList(self, node):
        if node is None:
            return 
        self.getLinkedList(node.left)
        self.head.right = node
        self.head = node
        self.getLinkedList(node.right)

#Ex1: can you implement it with a nonrecursive method ?
# read the article: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
# https://www.lintcode.com/problem/binary-tree-inorder-traversal/description

"""
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
"""

class InOrder(object):
    # inplace transform, return root 
    def inorderTraversal(self, root):
        # write your code here
        inorderList = []
        
        current = root
        stack = []
        
        while True:
            while current is not None:
                stack.append(current)
                current = current.left
            if len(stack) > 0:
                inorderList.append(stack.pop())
                current = inorderList[-1].right
            else: #len(stack) == 0
                break
        return [p.val for p in inorderList]
#
#Ex2: trim BST
#

class TrimBST:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trimBST(self, root, minimum, maximum):
        # write your code here
        if root is None:
            return None
        elif root.val < minimum:
            root = root.right
            return self.trimBST(root, minimum, maximum)
        elif root.val > maximum:
            root = root.left
            return self.trimBST(root, minimum, maximum)
        else:
            root.left = self.trimBST(root.left, minimum, maximum)
            root.right = self.trimBST(root.right, minimum, maximum)
            return root
    
    def trimBST2(self, root, minimum, maximum):
        # write your code here
        # this is another version
        if root is None:
            return None
            
        while root.val < minimum or root.val > maximum:
            if root.val < minimum:
                root = root.right
            else:
                root = root.left
            if root is None:
                return None

        root.left = self.trimBST(root.left, minimum, maximum)
        root.right = self.trimBST(root.right, minimum, maximum)
        return root

    def trimBST3(self, root, minimum, maximum):
        # write your code here
        # this is a failed version, why did it fail?
        # -- the order of condition is very important
        if root is None:
            return None
            
        while root.val < minimum:
            root = root.right
            if root is None:
                return None
        while root.val > maximum:
            root = root.left
            if root is None:
                return None
        root.left = self.trimBST(root.left, minimum, maximum)
        root.right = self.trimBST(root.right, minimum, maximum)
        return root
        
#
#Ex: insert Node 
#https://www.lintcode.com/problem/insert-node-in-a-binary-search-tree/description

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class InsertRemoveNode:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node
        
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                self.insertNode(root.right, node)
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                self.insertNode(root.left, node)
        
        return root

    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        pass



#
#4.7 Build Order
#https://leetcode.com/problems/course-schedule/description/
class Solution4_7(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.dic = {k:[] for k in range(numCourses)}
        for p, q in prerequisites:
            self.dic[q].append(p)
        self.visited = {}
        self.visiting = {}
        for n in self.dic.keys():
            if self.visited.get(n) is not None:
                continue
            if not self.noCycle_(n):
                return False
        return True
            
    def noCycle_(self, n):
        #print(n, self.visited)
        if self.visiting.get(n):
            return False
        else:
            self.visiting[n] = True
            
        for k in self.dic[n]:
            if self.visited.get(k):
                continue
            else:
                if not self.noCycle_(k):
                    return False
            
        self.visiting[n] = False
        self.visited[n] = True
        return True

# stack based topological sorting
class BuildOrder(object):
    
    @staticmethod
    def buildOrder(projectList, dependents):
        # create dependent list for each project
        dic = {p:[] for p in projectList}
        for p, q in dependents:
            dic[p].append(q)
        orderStack = []
        visiting = {}
        for p in projectList:
            if visiting.get(p) == 3:
                continue
            stack = [p]
            visiting[p] = 1
            while len(stack) > 0:
                #print(visiting)
                current = stack[-1]
                print("visit:", current)
                if visiting.get(current) == 2:
                    visiting[current] = 3 # means already visited
                    orderStack.append(stack.pop())
                    print("pop out:", current)
                elif visiting.get(current) ==1:
                    visiting[current] = 2
                    for node in dic[current]:
                        num = visiting.get(node)
                        if num == 2:
                            raise Exception("not DAG")
                        elif num == 3:
                            continue
                        else:
                            stack.append(node)
                            visiting[node] = 1
                            print('add:', node)
        return orderStack[::-1]


#Ex: can you use BFS for topological sorting?


#
#4.8 first common ancestor
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution4_8(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.left = p
        self.right = q
        
        _, _, anc = self.search_(root)
        
        if anc is not None:
            return anc
    
    def search_(self, node):
        if node is None:
            return False, False, None
        
        findleft1, findright1, anc = self.search_(node.left)
        if anc is not None:
            return True, True, anc
        
        findleft2, findright2, anc = self.search_(node.right)
        if anc is not None:
            return True, True, anc
        
        findleft = findleft1 or findleft2 or node.val == self.left.val
        findright = findright1 or findright2 or node.val == self.right.val
        if findleft and findright:
            return True, True, node
        else:
            return findleft, findright, None

#
#4.8 First Common ancestor-BST
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.minv = min(p.val, q.val)
        self.maxv = max(p.val, q.val)
        return self.BST(root, p, q)
        
    def BST(self, root, p, q):
        if root is None:
            return None
        elif root.val < self.minv:
            return self.BST(root.right, p, q)
        elif root.val > self.maxv:
            return self.BST(root.left, p, q)
        else:
            return root

#
#4.9 BST Sequence
#a hard problem 
# https://stackoverflow.com/questions/21211701/given-a-bst-and-its-root-print-all-sequences-of-nodes-which-give-rise-to-the-sa

"""
first, write an algo.(sub-problem is so called weaving) 
for listing all permutations for 
merging any two distinct value sequences;
then do a divide conquer for BST.

in order to do the sub-problem, we need to solve a more classic problem
how to list all probabilities of C(m,n).
- using dynamic programing (bfs)
- using dfs (listing by trim)
"""
class BSTSequence(object):
    def __init__(self, root):
        pass




if __name__ == "__main__":
    project = [0,1, 2, 3, 4]
    dependents = [[0,1], [0,2], [1,2], [2,3], [3,4], [0, 4]]
    print(BuildOrder.buildOrder(project, dependents))
