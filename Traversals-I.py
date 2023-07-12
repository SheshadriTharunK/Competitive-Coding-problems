'''TreeTraversal-I
Problem
Submissions
Leaderboard
Discussions
Given a random binary tree of N nodes in edge list format, you need to construct tree and display preorder, inorder, postorder and level order of node elements.

Input Format

First line contains two integers, N and X, number of nodes in the tree and value of the root.

Next 2*(N-1)lines contain details of nodes. Each detail of node contains two lines. First lines contains a string and second line contains an integer, which denotes the path of the node and the value of the node respectively.

String consists of only L or R. L denotes left child and R denotes right child.

Constraints

1 <= N <= 1000

1 <= value of node < 100

Output Format

Display four lines consisting of pre, in, post and level order of tree elements respectively.

Sample Input 0

5 1
L
2
R
3
LL
4
LR
5
Sample Output 0

1 2 4 5 3
4 2 5 1 3
4 5 2 3 1
1 2 3 4 5

 
'''

from collections import deque

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, path, val):
    if root is None:
        return TreeNode(val)
    rootcopy = root
    for i in range(len(path)-1):
        if path[i] == 'L':
            root = root.left
        else:
            root = root.right
    if path[-1] == 'L':
        root.left = TreeNode(val)
    else:
        root.right = TreeNode(val)
    return rootcopy

def preorderdisplay(root):
    if root is None:
        return
    print(root.val, end=' ')
    preorderdisplay(root.left)
    preorderdisplay(root.right)

def inorderdisplay(root):
    if root is None:
        return
    inorderdisplay(root.left)
    print(root.val, end=' ')
    inorderdisplay(root.right)
    
def postorderdisplay(root):
    if root is None:
        return
    postorderdisplay(root.left)
    postorderdisplay(root.right)
    print(root.val, end=' ')

def levelorder(root):
    if not root:
        return []

    q = deque()
    l = []
    q.append(root)

    while q:
        count = len(q)

        for _ in range(count):
            a = q.popleft()
            l.append(a.val)

            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)

    for i in l:
        print(i,end=' ')

def main():
    n, val = map(int, input().split())
    root = None
    root = insert(root, '', val)
    for i in range(n-1):
        path = input()
        val = int(input())
        root = insert(root, path, val)
    preorderdisplay(root)
    print(end='\n')
    inorderdisplay(root)
    print(end='\n')
    postorderdisplay(root)
    print(end='\n')
    levelorder(root)

main()
