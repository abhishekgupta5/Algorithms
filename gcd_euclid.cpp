#include<bits/stdc++.h>
using namespace std;

int euclid_gcd(int dividend, int divisor){
//It doesn't matter which is greater as after first iteration they will be rearranged automatically
    int rem;
    while(divisor != 0){
        int remainder = dividend%divisor;
        dividend = divisor;
        divisor = remainder;
        }
    return dividend;
    }

//Recursive way
int euclid_gcd_recursive(int a, int b){
    return b == 0 ?  a : euclid_gcd_recursive(b, a%b);
    }


main(){

    int a, b;
    cout<<"Enter 2 numbers to find GCD: ";
    cin>>a>>b;
    int gcd = euclid_gcd(a,b);
    cout<<endl<<gcd<<endl;
    }
