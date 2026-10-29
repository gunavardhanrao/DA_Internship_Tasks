# https://www.hackerrank.com/challenges/python-lists/problem
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

N = int(input())

lst = []

for i in range(N):
    
    command = input().split()
    
    if command[0] == "insert":
        lst.insert(int(command[1]),int(command[2]))
    if command[0] == "remove":
        lst.remove(int(command[1]))
    if command[0] == "print":
        print(lst)
    if command[0] == "append":
        lst.append(int(command[1]))
    if command[0] == "sort":
        lst.sort()
    if command[0] == "pop":
        lst.pop()
    if command[0] == "reverse":
        lst.reverse()
