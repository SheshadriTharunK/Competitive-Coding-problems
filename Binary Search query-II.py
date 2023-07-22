'''BSTQuery-II
Implement the following operations on a binary search tree(bst) with distinct integers:

add(root, val): add a node with val to the bst and return root. Display ADD SUCCESS if addition is successful otherwise display DUPLICATE FOUND.
remove(root, val): remove a node with val from bst and return root. Display REMOVE SUCCESS if removal is successful otherwise display NOT FOUND.
display(root): display the elements of the bst in the pretty form. If tree is empty, display blankline.
Assume that the root refers to the root node of bst.

Input Format

First line consists of number N of operations on bst.

Next N lines consists of N operations to be performed on the bst.

Constraints

1 <= N <= 100

Output Format

Print the output as expected for each operation.

Sample Input 0

8
1 50
1 40
1 60
2 40
3
2 100
1 200
3
Sample Output 0

ADD SUCCESS
ADD SUCCESS
ADD SUCCESS
REMOVE SUCCESS
50
  60(R)
NOT FOUND
ADD SUCCESS
50
  60(R)
    200(R)'''

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
    else:
        print("DUPLICATE FOUND")

    return root

def find_min(node):
    while node.left:
        node = node.left
    return node

def remove(root, val):
    if root is None:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            min_right = find_min(root.right)
            root.val = min_right.val
            root.right = remove(root.right, min_right.val)

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
n = int(input())
for i in range(n):
    op =  input().split()
    if op[0] =='1':
        if int(op[1]) in l:
            print("DUPLICATE FOUND")
        else:
            val = int(op[1])
            root = add(root, val)
            l.append(val)
            print("ADD SUCCESS")
    elif op[0] == '3':
        display(root, 0, '')
    elif op[0] == '2':
        val = int(op[1])
        if val in l:
            print("REMOVE SUCCESS")
            root = remove(root, val)
            l.remove(val)
        else:
            print("NOT FOUND")
