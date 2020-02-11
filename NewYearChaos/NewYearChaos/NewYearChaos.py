def minimumBribes(q):
    res=0
    flag=True
    for x in range(len(q) - 1, -1, -1):
        
        if (q[x]!=x+1):
            if (q[x-1]==x+1):
                res+=1
                t=q[x]
                q[x]=q[x-1]
                q[x-1]=t
            elif (q[x-2]==x+1):
                res+=2
                t=q[x]
                q[x]=q[x-2]
                q[x-2]=q[x-1]
                q[x-1]=t
            else: 
                print("Too chaotic")
                flag=False
                break
    if (flag):
        print(res)
