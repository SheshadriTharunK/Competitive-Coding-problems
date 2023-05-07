T=int(input())
for i in range(T):
    px,py,qx,qy=map(int,input().split())
    print(2*qx-px,2*qy-py)
    '''consider two points,p=(px,py) and q=(qx,qy).we consider the inversion or point reflection ,r=(rx,ry),of point p across point q to be a 180 degree rotation of point p around q'''