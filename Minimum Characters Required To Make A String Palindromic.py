# Given an string A. The only operation allowed is to insert  characters in the beginning of the string.

# Find how many minimum characters are needed to be inserted to make the string a palindrome string.

# Input Format

# The only argument given is string A.
# Output Format

# Return the minimum characters that are needed to be inserted to make the string a palindrome string.
# For Example

# Input 1:
#     A = "ABC"
# Output 1:
#     2
#     Explanation 1:
#         Insert 'B' at beginning, string becomes: "BABC".
#         Insert 'C' at beginning, string becomes: "CBABC".

# Input 2:
#     A = "AACECAAAA"
# Output 2:
#     2
#     Explanation 2:
#         Insert 'A' at beginning, string becomes: "AAACECAAAA".
#         Insert 'A' at beginning, string becomes: "AAAACECAAAA".


# %%
def solve(a):
    x = a + '-' + a[::-1]
    p, t = 0, [-1]*len(x)
    for i in range(1, len(x)):
        if x[i]==x[p]:
            t[i] = t[p]
        else:
            t[i] = p
            while p>=0 and x[i]!=x[p]:
                p = t[p]
        p = p + 1
    return len(a)-p

solve('aba')

# cba
# abc

# %%
