'''Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring consisting of non-space characters only.'''

def len_of_last_word(s):
    words = s.strip().split()
    if not words:
        return 0, None
    last_word = words[-1]
    return len(last_word), last_word

s = input("Enter the string: ")
llw, lw = len_of_last_word(s)
print("Output:", llw)
if lw is not None:
    print(f'The length of the last word "{lw}" is {llw}')
else:
    print("No words in the input string.")
