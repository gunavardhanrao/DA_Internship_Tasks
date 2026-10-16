# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    
  a = line.split()
  
  a = '-'.join(a)
  
  return a
