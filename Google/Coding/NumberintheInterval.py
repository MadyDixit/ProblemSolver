
'''
Objective: Given a list of intervals with start and end for each interval. You have given a value V, write an algorithm to find the number of intervals in which the value V lies.

Example:

Given Interval: [[1,7], [3,10], [12,15]]
Value : 6 lies in Intervals: 2

Given Interval: [[1,7], [3,10], [12,15]]
Value : 11 lies in Intervals: 0
'''

'''Approach'''
n = int(input('Enter the Number of Interval:'))
l = []
for i in range(n):
    m, n = input().split(' ')
    l.append([int(m),  int(n)])
v = int(input())
count = 0
for i in range(len(l)):
    if l[i][0] < v and l[i][1] > v:
        count += 1
print(count)
