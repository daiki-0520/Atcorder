#include <bits/stdc++.h>
#define repr(i, n) for(int i = n; i >= 0; i--)
#define rep(i, m, n) for(int i = m; i < n; i++)
#define inf 2e9
#define all(v) v.begin(), v.end()
#define fore(i,a) for(auto &i:a)
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
using namespace std;
typedef long long ll;
int main(){
    int ans = inf;
    int N;
    int A[1010101010],P[1010101010],X[1010101010];
    cin >> N;
    rep(i,0,N) cin >> A[i] >> P[i] >> X[i];
    rep(i,0,N){
        if(A[i]<X[i]){
            chmin(ans,P[i]);
        } 
    if(ans == inf) ans=-1;
    cout << ans << endl;
    return 0;
}