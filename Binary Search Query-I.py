'''BSTQuery-I

Implement the following operations on a binary search tree(bst) with distinct integers:

add(root, val): add a node with val to the bst and return root. Display ADD SUCCESS if addition is successful otherwise display DUPLICATE FOUND.
display(root): display the elements of the bst in the pretty form as shown in sample. If tree is empty, display blankline.
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
1 40
2
1 100
1 200
2
Sample Output 0

ADD SUCCESS
ADD SUCCESS
ADD SUCCESS
DUPLICATE FOUND
50
  40(L)
  60(R)
ADD SUCCESS
ADD SUCCESS
50
  40(L)
  60(R)
    100(R)
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
        if  int(op[1]) in l:
            print("DUPLICATE FOUND")
        else:
            val=int(op[1])
            root = add(root, val)
            l.append(val)
            print("ADD SUCCESS")
    else :
        display(root, 0, '')