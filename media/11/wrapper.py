n = int(input(""))
arr = [int(x) for x in input("").strip().split(" ")]

maxSum = []
maxSum.append(arr[0])
sMax = -99999999999
for i in range(1,n):
    maxSum.append(max(arr[i],maxSum[i-1]+arr[i]))
for j in maxSum:
    sMax = max(sMax,j)

print(sMax)