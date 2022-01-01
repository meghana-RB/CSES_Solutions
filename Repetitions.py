inputStr = input()
firstPointer = 0
endPointer = 0
maxi = 1
 
while firstPointer < len(inputStr) and endPointer < len(inputStr):
    if inputStr[firstPointer] == inputStr[endPointer]:
      endPointer = endPointer + 1
      maxi = max(maxi, endPointer - firstPointer)
    else :
      firstPointer = endPointer
 
print(maxi)