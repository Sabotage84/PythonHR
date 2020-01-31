def alternatingCharacters(s):
    t=s[0]
    i=1
    res=0
    while (i<len(s)):
        if (t==s[i]):
            res+=1
        else:
            t=s[i]
        i+=1
    return res