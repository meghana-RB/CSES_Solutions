#Solution to task https://cses.fi/problemset/task/1094
length = int(input())
inputArray = [int(x) for x in (input()).split()]
sum = 0
for i in range(1,length):
  if inputArray[i-1] > inputArray[i]:
    sum = sum + inputArray[i-1] - inputArray[i]
    inputArray[i] = inputArray[i-1]
print(sum)
