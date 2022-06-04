# cook your dish here
n=int(input())
X=Y=0
L=0
for _ in range(n):
    si,ti=tuple(map(int,input().split()))
    X += si
    Y += ti
    l=abs(X-Y)
    if l>L:
        L=l
        W=1 if X>Y else 2
print(W,L)
