'''
#python version : 3.8

Problem Description
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.

Problem Constraints
0 <= A.size() <= 700000
1 <= A[i] <= 107

Input Format
The first and the only argument is an array of integers, A.

Output Format
Return an integer, representing the maximum possible profit.

Example Input
Input 1:
A = [1, 2]
Input 2:

A = [1, 4, 5, 2, 4]

Example Output
Output 1:
1
Output 2:

4

Example Explanation
Explanation 1:
Buy the stock on day 0, and sell it on day 1.
Explanation 2:

Buy the stock on day 0, and sell it on day 2.
'''


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):

        n = len(A)
        max_prof = 0
        if n==0:
            return max_prof
        max_val = max(A)
        min_val = min(A)
        if min_val == max_val:
            return max_prof
        i = 0
        while(i<n):
            if i == n-1:
                j = i 
            else:
                j = i+1

            mx_val=max(A[j:n])
            prof = mx_val-A[i]
            if prof > 0:
                max_prof = max(max_prof,prof)
            i+=1
        return max_prof

if __name__ == "__main__":
    # This code will only be executed 
    # if the script is run as the main program
    A = [2,1,3,5,4] #Input val
    obj = Solution(A)
    max_prof = obj.maxProfit()
    print(f"Input : {A}\n Max Profit : {max_prof}")

