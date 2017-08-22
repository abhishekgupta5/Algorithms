# include<bits/stdc++.h>
using namespace std;

void prime_factorization(int n){
    int max_num = ceil(sqrt(n));
    for (int i=2; i<=max_num; i++){
        if (n%i == 0){
            int count = 0;
            while(n%i == 0){
                n=n/i;
                count++;
                }
            cout<<i<<"^"<<count<<" ";
            }
        }
    if (n != 1){
        cout<<n<<"^1";
        }
    cout<<endl;
    }

main(){
    cout<<"Enter number: ";
    int n;
    cin>>n;
    prime_factorization(n);
    }
