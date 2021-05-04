#include <bits/stdc++.h>
#define repr(i, n) for(int i = n; i >= 0; i--)
#define rep(i, m, n) for(int i = m; i < n; i++)
#define inf 2e9
#define all(v) v.begin(), v.end()
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
using namespace std;
typedef long long ll;
int main(){
    int a,b,w;
    cin >> a >> b >> w;
    int m=inf, M=0;
    rep(i,1,1000000){
        if(a*n<=1000*w && 1000*w<=b*n){
            m=chmin(m,n);
            M=chmax(M,n);
        }
    }
    if(M==0)cout << "UNSATISFIABLE";
    else cout << m << ' ' << M;
}