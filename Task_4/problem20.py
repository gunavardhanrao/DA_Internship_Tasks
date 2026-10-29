# https://www.hackerrank.com/challenges/no-idea/problem
# There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is .
# For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.


n, m = input().split()

arr = input().split()

A = set(input().split())

B = set(input().split())

happiness = 0


for i in arr:
    
    if i in A:
        
        happiness += 1
        
    if i in B:
        
        happiness -=1
        

print(happiness)

