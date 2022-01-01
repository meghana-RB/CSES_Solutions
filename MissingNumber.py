#Solution to https://cses.fi/problemset/task/1083

num = input()
listOfNums = [int(x) for x in (input()).split()]
 
listOfNums.sort()
 
if int(num) == 2:
  if listOfNums[0] < int(num):
    print(num)
  else:
    print(listOfNums[0] - 1)
else:
  for i in range (len(listOfNums) - 1):
    if listOfNums[i+1] != (listOfNums[i] + 1):
      print(listOfNums[i] + 1)
      break
    if i == (len(listOfNums) - 2) :
      print(listOfNums[i+1] + 1)
