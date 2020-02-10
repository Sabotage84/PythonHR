q=[2, 1, 5, 3, 4]
res=0
index=len(q)
i=0
s=reversed(q)
for x in s:
    print(s)
    if (x!=index):
        if (q[i+1]==index):
            res+=1
            t=x
            q[i]=q[i+1]
            q[i+1]=t
        elif (q[i+2]==index):
            res+=2
            t=x
            q[i]=q[i+2]
            q[i+2]=q[i+1]
            q[i+1]=x
        else: 
            print("Too chaotic")
    i+=1
    index-=1



print(res)
