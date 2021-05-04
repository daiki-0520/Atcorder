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
    ll N,ans=0;
    cin >> N;
    if(N>=1'000) ans+=N-999;
    if(N>=1'000'000) ans+=N-999'999;
    if(N>=1'000'000'000) ans+=N-999'999'999;
    if(N>=1'000'000'000'000) ans+=N-999'999'999'999;
    if(N>=1'000'000'000'000'000) ans+=N-999'999'999'999'999;
    cout << ans << endl;
}