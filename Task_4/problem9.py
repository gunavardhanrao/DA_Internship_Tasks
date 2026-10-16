# https://www.hackerrank.com/challenges/python-mutations/problem
# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    
  lst = list(string)
  
  lst[position] = character
  
  string = "".join(lst)
  
  return string
