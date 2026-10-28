# https://www.hackerrank.com/challenges/py-set-add/problem
# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

n = int(input())

country = set()

for i in range(n):
    
    country.add(input())
    
print(len(country))
