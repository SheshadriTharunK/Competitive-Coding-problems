class TreeNode():
    def __init__(self,val):
        self.val=val 
        self.left=None 
        self.right=None 
        
def insert(root,path,val):
    if root==None :
        return TreeNode(val)
    rootcopy=root 
    for i in range(len(path)-1):
        if path[i]=='L':
            root=root.left
        else:
             root=root.right
    if path[-1]=='L':
         root.left=TreeNode(val)
    else:
        root.right=TreeNode(val)
    return rootcopy
def display(root,nspaces,label):
    if root==None:
        return 
    
    for i in range(nspaces):
        print(' ',end='')
        
    print(root.val,end='')
    if label!=' ':
        print('(',label,')',sep='')
    else:
        print()
    display(root.left,nspaces+2,'L')
    display(root.right,nspaces+2,'R')
    
    
    
    
    
def main():
    n,val=map(int,input().split())
    root=None 
    root=insert(root,'',val)
    for i in range(n-1):
        path=input()
        val=int(input())
        root=insert(root,path,val)
    display(root,0,' ')
main()