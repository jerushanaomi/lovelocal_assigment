'''Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.'''
def count_one(n):
    c = 0
    for i in range(n + 1):
        c += str(i).count('1')
    return c
n = int(input("Enter an integer: "))
res = count_one(n)
print(f"The total number of digit 1 appearing in all non-negative integers less than or equal to {n} is {res}.")
