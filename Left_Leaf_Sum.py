class TreeNode:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
def insert(root,a):
    if a:
        val=a.pop(0)
        if val!='#':
            root=TreeNode(int(val))
            root.left=insert(root.left,a)
            root.right=insert(root.right,a)
        else:
            return None 
    return root 
def sum1(root,m,d):
    if root is None:
        return  
    elif d=='L' and root.left is None and root.right is None: 
        m[0]+=root.data 
    sum1(root.left,m,'L')
    sum1(root.right,m,'R')
    return m[0]
import sys 
sys.setrecursionlimit(100000)
def main():
    t=int(input())
    for i in range(t):
        root=None 
        a=input().split()
        root=insert(root,a)
        m=[0]
        print(sum1(root,m,'d'))
main()
