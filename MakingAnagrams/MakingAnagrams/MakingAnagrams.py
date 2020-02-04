def makeAnagram(a, b):
    dict_a={}
    dict_b={}
    res=0
    for x in a:
        if (x in dict_a):
            dict_a[x]+=1
        else:
            dict_a[x]=1

    for x in b:
        if (x in dict_b):
            dict_b[x]+=1
        else:
            dict_b[x]=1

    for w in dict_a:
        if (w in dict_b):
            res+=abs(dict_a[w]-dict_b[w])
        else:
            res+=dict_a[w]
    for x in dict_b:
        if (x not in dict_a):
            res+=dict_b[x]
    return res
