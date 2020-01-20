def hourglassSum(arr):
  maxSum=arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2]
    for y in range(0,4):
        for x in range(0,4):
            tempSum=arr[y][x]+arr[y][x+1]+arr[y][x+2]+arr[y+1][x+1]+arr[y+2][x]+arr[y+2][x+1]+arr[y+2][x+2]
            if(tempSum>maxSum):
                maxSum=tempSum
    return maxSum
