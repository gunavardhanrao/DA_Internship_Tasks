# https://www.hackerrank.com/challenges/nested-list/problem
# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

records = []
scores = set()

for i in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    scores.add(score)
    
sorted_scores = sorted(scores)
second_low_score = sorted_scores[1]

names = []
for name, score in records:
    if score == second_low_score:
        names.append(name)
        
for name in sorted(names):
    print(name)
