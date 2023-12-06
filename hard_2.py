'''You are given a string s. You can convert s to a 
palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation'''
def shortest_palindrome(s):
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1

    return s[i:][::-1] + s

input_string = input("Enter the string: ")
result = shortest_palindrome(input_string)
print(f"The shortest palindrome is: {result}")
