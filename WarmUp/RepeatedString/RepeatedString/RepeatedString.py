def repeatedString(s, n):
    aCount=0;
    res=0;
    for x in s:
        if(x=='a'):
            aCount+=1;
    f=n//len(s)
    if(f==0):
        for x in range(n):
            if (s[x]=='a'):
                res+=1;
        return res
    else:
        res+=(aCount*f)
        t=n- f*len(s)
        for x in range(t):
            if (s[x]=='a'):
                res+=1
        return res
