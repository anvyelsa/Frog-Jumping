t=int(input())
for i in range(t):
    a,b,k=map(int,input().split())   
    if k%2==0:
        a=a*(k//2)
        b=b*(k//2)    
        print(a-b)
    elif k%2!=0:
        a=a*(k//2+1)
        b=b*(k//2)
        print(a-b)
    