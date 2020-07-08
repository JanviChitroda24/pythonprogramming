'''
Objective 
In this challenge, we practice calculating standard deviation. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given an array, , of  integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of  decimal place (i.e.,  format). An error margin of  will be tolerated for the standard deviation.

Input Format

The first line contains an integer, , denoting the number of elements in the array. 
The second line contains  space-separated integers describing the respective elements of the array.

Constraints

, where  is the  element of array .
Output Format

Print the standard deviation on a new line, rounded to a scale of decimal place (i.e.,  format).

Sample Input

5
10 40 30 50 20
Sample Output

14.1
Explanation

First, we find the mean: 
Next, we calculate the squared distance from the mean, , for each :

Now we can compute , so:

Once rounded to a scale of  decimal place, our result is .
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(input())
arr = list(map(int, input().split()))

mean = sum(arr)/len(arr)

sum = 0
for i in range(len(arr)):
    sum += (arr[i] - mean) ** 2

print(round(math.sqrt(sum / len(arr)), 1))