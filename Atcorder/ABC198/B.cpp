#include <bits/stdc++.h>
#define repr(i, n) for(int i = n; i >= 0; i--)
#define rep(i, m, n) for(int i = m; i < n; i++)
#define inf 2e9
#define ALL(v) v.begin(), v.end()
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
using namespace std;
typedef long long ll;
int main(){
    string N;
    cin >> N;
    while(*N.rbegin()=='0') N=N.substr(0,N.length()-1);
    string NN = N;
    reverse(ALL(NN));
    if(N == NN) cout << "YES" << endl;
    else cout << "NO" << endl;
}