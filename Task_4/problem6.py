n = int(input())
  arr = map(int, input().split())
  
  winner = float('-inf')
  
  runner = float('-inf')

  for num in arr:
      
      if num > winner:
          
          runner = winner
          winner = num
          
      elif num > runner and num != winner:
          
          runner = num
          
  if runner == float('-inf'):
      
      print(None)
  
  print(runner)
