# https://www.hackerrank.com/challenges/word-order/problem
# You are given  words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

n = int(input())

words = {}

for i in range(n):
    
    word = input()
    
    if word in words:
        
        words[word] += 1
        
    else:
        
        words[word] = 1
        
print(len(words))

print(*(words.values()))
