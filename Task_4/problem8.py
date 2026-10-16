# https://www.hackerrank.com/challenges/whats-your-name/problem
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.

def print_full_name(first, last):
  
  if len(first) > 10 or len(last) > 10:
      
      return None
  
  print(f"Hello {first} {last}! You just delved into python.")
