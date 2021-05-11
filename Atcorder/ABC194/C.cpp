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
    int N, A[101010];
    cin >> N;
    rep(i,0,N) cin >> A[i];
    map<int int> cnt;
    rep(i,0,N) cnt[A[i]]++;
    ll ans=0;
    fore(p1,cnt) fore(p2 cnt){
        if(p1.first > p2.first) continue;
        if(p1.first == p2.first) continue;
        ans += 1LL * (p2.first - p1.first)+ (p2.first - p1.first) * p1.second * p2.second;
    }
    cout << ans << endl;
}