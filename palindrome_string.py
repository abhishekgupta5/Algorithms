#!/usr/bin/python3

#INterviewbit-Strings
#Question link: https://www.interviewbit.com/problems/palindrome-string/

def palindrome(S):
    S = "".join(ch.lower() for ch in S if ch.isalnum())
    size = len(S)
    for i in range(int(size/2)):
        if S[i] != S[size-i-1]:
            return False
    return True

if __name__ == '__main__':
    s = input("Enter string: ")
    print(palindrome(s))
