def jumpingOnClouds(c):
    res=0
    x=0
    while x<(len(c)):
        if (x==len(c)-1):
            return res
        if (x==len(c)-2):
            return res+1

        if (c[x+2]==0):
            res+=1
            x+=2
        else:
            res+=1
            x+=1
    res+=1
    return res


