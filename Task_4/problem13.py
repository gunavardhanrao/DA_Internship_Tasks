# https://www.hackerrank.com/challenges/symmetric-difference/problem
# Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

m = int(input())
list_1 = set(map(int, input().split()))
n = int(input())
list_2 = set(map(int, input().split()))

sym_diff = list_1.difference(list_2).union(list_2.difference(list_1))

for i in sorted(sym_diff):
    
    print(i)
