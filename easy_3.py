'''Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it'''
def pascal(numRows):
    if numRows <= 0:
        return []

    tri = [[1]]

    for i in range(1, numRows):
        row = [1]
        prev_row = tri[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        tri.append(row)

    return tri

numRows = int(input("Enter the number of rows for Pascal's triangle: "))
result = pascal(numRows)
print("Output", result)
