
A=[2, -1, -2, 3, 4, -5]   
curSum=0
startI=0
endI=0
maxSum=None
endIndex=0
startIndex=0

for x in A:
    curSum+=x

    if (maxSum==None or curSum>maxSum):
        maxSum=curSum
        startIndex=startI
        endIndex=endI
    if (curSum<0):
        curSum=0
        startI=endI+1
    endI+=1

print(maxSum, startIndex, endIndex)

input()
  