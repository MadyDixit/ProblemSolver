'''
Find the Longest Common Subsequence Length Using Recursion.
'''

def LCSLenghtR(x, y):
    '''
    :param x: First String
    :param y: Second String
    :return: Length of Common SubSequence
    '''
    #If length of string is 0 then return 0
    if(len(x) == 0 or len(y) == 0):
        return 0
    #if last element matches of the Array then
    if x[-1] == y[-1]:
        return LCSLenghtR(x[:-1],y[:-1]) + 1
    #else if the last element don't match then
    return max(LCSLenghtR(x,y[:-1]), LCSLenghtR(x[:-1],y))
'''
Find the Longest Common Subsequence using Dynamic Programming (Bottom-UP Approach (Tabulation)).
'''


def lcsDP(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]
    print(L)
    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# end of function lcs


'''
Find the Longest Common Sequence using Dynamic Programming using Memoization.
'''


def lcs(X, Y, m, n, dp):
    # base case
    if (m == 0 or n == 0):
        return 0

    # if the same state has already been
    # computed
    if (dp[m - 1][n - 1] != -1):
        return dp[m - 1][n - 1]

        # if equal, then we store the value of the
    # function call
    if (X[m - 1] == Y[n - 1]):

        # store it in arr to avoid further repetitive
        # work in future function calls
        dp[m - 1][n - 1] = 1 + lcs(X, Y, m - 1, n - 1, dp)

        return dp[m - 1][n - 1]

    else:

        # store it in arr to avoid further repetitive
        # work in future function calls
        dp[m - 1][n - 1] = max(lcs(X, Y, m, n - 1, dp),
                               lcs(X, Y, m - 1, n, dp))

        return dp[m - 1][n - 1]
if __name__ == '__main__':
    maximum = 1000
    x = 'ABCBDAB'
    y = 'BDCABA'
    m = len(x)
    n = len(y)
    print('The Longest Subsequqence in given String ',x,' and ',y,' is ',LCSLenghtR(x,y))
    print('The Longest Subsequqence in given String ',x,' and ',y,' is ',lcsDP(x,y))
    dp = [[-1 for _ in range(maximum)]for _ in range(m)]
    print('The Longest Subsequqence in given String ',x,' and ',y,' is ',lcs(x,y,m,n,dp))
