# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.


def average(array):
    # your code goes here
    
    average = sum(set(array)) / len(set(array))
    
    return average
