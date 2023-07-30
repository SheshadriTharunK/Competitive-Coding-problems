'''PreOrderToBST

Given a random binary search tree of size N in the preorder format, you need to construct tree and print the tree in pretty form.

Input Format

A single line consisting of preorder representation of binary search tree.

Constraints

1 <= N <= 1000

Output Format

Refer to sample output.

Sample Input 0

50 20 10 30 70
Sample Output 0

50
  20(L)
    10(L)
    30(R)
  70(R)'''


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def add(root, val):
    if root is None:
        return TreeNode(val)

    if val > root.val:
        root.right = add(root.right, val)
    elif val < root.val:
        root.left = add(root.left, val)
   

    return root

def display(root, nspaces, path):
    if root is None:
        return

    for i in range(nspaces):
        print(' ', end='')

    print(root.val, end='')
    if path != '':
        print('(', path, ')', sep='')
    else:
        print()
    display(root.left, nspaces + 2, 'L')
    display(root.right, nspaces + 2, 'R')

l = []
root = None
a=list(map(int,input().split()))
for i in a:
    root=add(root,i)
display(root,0,'')
