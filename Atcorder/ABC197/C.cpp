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
    int N, A[20];
    cin >> N;
    rep(i,0,N) cin >> A[i];
    if(N == 1){
        cout << A[0] << endl;
        return 0;
    }
    int ans = inf;
    rep(bit, 0, 1 << (N-1)){
        int a_xor = 0;
        int a_or = A[0];
        rep(i,1,N){
            if(bit & (1 << (i-1))){
                a_xor ^= a_or;
                a_or=0;
            }
            a_or |= A[i];
        }
        a_xor ^= a_or;
        chmin(ans,a_xor);
    }
    cout << ans << endl;
    return 0;
}