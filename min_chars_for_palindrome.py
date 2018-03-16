#!/usr/bin/python3

#Interviewbit-strings
#Question: https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/

def minChars(s):
    s = ''.join(reversed(s))
    size = len(s)
    for i in range(size):
        sub_list = s[i::]
        if (sub_list == sub_list[::-1]):
            return i

if __name__ == '__main__':
    s = input('Enter string: ')
    print(minChars(s))
