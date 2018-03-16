#!/usr/bin/python3

#Interviewbit-Strings
#Question link: https://www.interviewbit.com/problems/reverse-the-string/

def reverse(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    s = input('Enter string: ')
    print(reverse(s))
