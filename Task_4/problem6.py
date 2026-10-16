# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

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
