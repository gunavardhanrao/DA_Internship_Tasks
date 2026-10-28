# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

n = int(input())
student_marks = {}

for _ in range(n):
    
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    
query_name = input()

scores_list = student_marks.get(query_name)

avg = sum(scores_list) / len(scores_list)

print(f"{avg:.2f}")
