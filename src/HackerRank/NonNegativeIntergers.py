# Task
# The provided code stub reads and integer, , from STDIN.
# For all non-negative integers , print .
#
# Example
#
# The list of non-negative integers that are less than  is .
# Print the square of each number on a separate line.
#
# 0
# 1
# 4
# Input Format
#
# The first and only line contains the integer, n.
#
# Constraints
#
#
# Output Format
#
# Print  lines, one corresponding to each i.
#
# Sample Input 0
#
# 5
# Sample Output 0
#
# 0
# 1
# 4
# 9
# 16

n = 3
squares = [i ** 2 for i in range(n)]
for num in squares:
    print(num)