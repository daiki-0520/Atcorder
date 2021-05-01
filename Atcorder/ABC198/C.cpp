#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < n; i++)
#define repr(i, n) for(int i = n; i >= 0; i--)
#define rep(i, m, n) for(int i = m; i < n; i++)
#define inf 2e9
#define all(v) v.begin(), v.end()
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
using namespace std;
typedef long long ll;
int main(){
    double R, X, Y;
    cin >> R >> X >> Y;
    double distance = sqrt(X*X+Y*Y);
    int ans = ceil(distance / R);
    if(ans == 1 && distance != R) ans++;

    cout << ans << endl;
}