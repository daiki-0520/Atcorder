#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < n; i++)
#define repr(i, n) for(int i = n; i >= 0; i--)
#define rep(i, m, n) for(int i = m; i < n; i++)
#define INF 2e9
#define ALL(v) v.begin(), v.end()
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
using namespace std;
typedef long long ll;
int main(){
    int N, A[100],B[100];
    cin >> N;
    rep(i,0,N) cin >> A[i];
    rep(i,0,N) cin >> B[i];
    int left = -inf, right=inf;
    rep(i,0,N){
        max(left,A[i]);
        min(right,B[i]);
    }
    int ans=max(0,right-left+1);
    cout << ans << endl;
}