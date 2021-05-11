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
    int N, A[1010],B[1010];
    cin >> N;
    rep(i,0,N) cin >> A[i] >> B[i];
    int ans=inf;
    rep(a,0,N) rep(b,0,N){
        int cost;
        if(a==b) cost=A[a] + B[b];
        else cost=max(A[a],B[b]);
        chmin(ans,cost);
    }
    cout << ans << endl;
}