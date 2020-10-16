//Optimized prime sieve algorithm to find prime numbers from 0 to N range

#include <bits/stdc++.h>
using namespace std;

#define pb      push_back
#define ff      first
#define ss      second
#define ll      long long
#define f(i,n)  for(int i = 0; i < n; i++)
#define F(i,n)  for(ll i = 0; i < n; i++)
#define endl    '\n'
#define mod     1000000007
#define rex     ios_base::sync_with_stdio(0);cin.tie(0)
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pll;
typedef vector<int>		vi;
typedef vector<ll>		vll;
typedef vector<string>  vs;
typedef vector<pii>     vpii;
typedef vector<pll>     vpll;
const double PI = 3.141592653589793238460;

int main()
{
    ll kMaxValue = 10000;
    vll primes;
    primes.pb(2);


    //optimized prime sieve
    for(ll i = 3; i < kMaxValue; i += 2)
    {
        bool isPrime = true;
        for(auto p : primes)
        {
            if(p*p > i)
                break;
            if(i % p == 0)
            {
                isPrime = false;
                break;
            }
        }
        if(isPrime)
            primes.pb(i);
    }
 
    cout<<primes.size(); 
    return 0;
}
