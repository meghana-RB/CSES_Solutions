n = int(input())

if n == 3 or n==2:
  print("NO SOLUTION")
else:
  print(*[x for x in range(2, n+1, 2)], *[x for x in range(1, n+1, 2)])