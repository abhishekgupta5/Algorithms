# include<bits/stdc++.h>
using namespace std;


void sieve(int n){
    int prime[n+1];
//Setting every number as prime(1 for prime, 0 for non-prime)
    for (int i=0; i<=n; i++){
    //This loop is O(n)
    prime[i] = 1;
        }
        prime[0] = 0;
        prime[1] = 0;
    int max_factor = ceil(sqrt(n));

    for (int i=2 ; i<=max_factor ; i++){
    //This loop is O(n*log(log(n)))
        if (prime[i] == 1){
            for (int j=2; i*j<=n; j++){
                prime[i*j] = 0;
                }
            }
        }
    //Overall complexity O(n*loglog(n))

    //Printing the numbers
    for (int i=0; i<=n; i++){
        if (prime[i])
            cout<<i<<" ";
        }
    cout<<endl;
    }

main(){
    int n;
    cout<<"Enter number: ";
    cin>>n;
    cout<<endl;
    sieve(n);
    }
