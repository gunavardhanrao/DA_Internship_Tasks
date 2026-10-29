# https://www.hackerrank.com/challenges/collections-counter/problem
#  is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.

from collections import Counter

n = int(input())

shoe_size = Counter(input().split())

m = int(input())

money_earned = 0

for i in range(m):
    
    shoe_and_price = input().split()
    
    if shoe_size[shoe_and_price[0]] != 0:
        
        money_earned += int(shoe_and_price[1])
        
        shoe_size[shoe_and_price[0]] -= 1
        
print(money_earned)
