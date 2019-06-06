# DAY 1
def func(arr,num):
  for i in range (0, len(arr) -1):
    for j in range (1, len(arr)):
      if arr[i] + arr[j] == num:
        return True
      
  return False