"""Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area."""


def maximal_square(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                max_side = max(max_side, dp[i][j])

    return max_side * max_side

matrix = [
    list(row.strip("[]").replace('"', "").split(","))
    for row in input("Enter the binary matrix elements in the specified format: ")
    .strip("[]")
    .split("],[")
]

result = maximal_square(matrix)
print(f"Output: {result}")
