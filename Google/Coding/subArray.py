"""
Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.
Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4
Simple Method
"""
def subArray(l,s):
    """
    :param l: List of Element
    :param s: Sum to be Found in the List
    :return: Index Value of Array at which it start and End
    """
    for i in range(0,len(l)):
        curr_sum = l[i]
        for j in range(i+1,len(l)):
            if curr_sum == s:
                print('Sum Found:',i ,' and ', j-1)

                return 1
            else:
                curr_sum += l[j]
    print('No SubArray Found')
    return 0

subArray([1, 4, 20, 3, 10, 5], 33)
