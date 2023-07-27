def location(S, low, high):
  if (low > high):
    return -1
  else:
    mid = (low + high) // 2
    if (x == S[mid]):
      return mid
    elif (x < S[mid]):
      return location(S, low, mid-1)
    else:
      return location(S, mid+1, high)
    
S = [10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45]
x = 40
loc = location(S, 1, len(S))
print(loc)