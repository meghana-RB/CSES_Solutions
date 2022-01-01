def weirdNum(num):
  print(num)
  if num == 1:
    return
  if num % 2 == 0:
    weirdNum(num//2)
  else:
    weirdNum( num*3 + 1)
 
num = input()
weirdNum(int(num))