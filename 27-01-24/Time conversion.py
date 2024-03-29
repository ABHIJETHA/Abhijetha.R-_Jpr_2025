'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
Submissions: 4
Max Score: 15
Difficulty: Easy
Rate This Challenge:

    
More
 
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
​
9
#
10
# Complete the 'timeConversion' function below.
11
#
12
# The function is expected to return a STRING.
13
# The function accepts STRING s as parameter.
14
#
15'''

def timeConversion(s):
17
    # Write your code here
18
​
19
if __name__ == '__main__':
20
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
21
​
22
    s = input()
23
​
24
    result = timeConversion(s)
25
​
26
    fptr.write(result + '\n')
27
​
28
    fptr.close()
29
​
