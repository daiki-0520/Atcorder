#include <bits/stdc++.h>
#define repr(i, n) for(int i = n; i >= 0; i--)
#define rep(i, m, n) for(int i = m; i < n; i++)
#define inf 2e9
#define all(v) v.begin(), v.end()
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
using namespace std;
typedef long long ll;
void main(){
    int H,W,X,Y;
    string S[101];
    int dx[4] = {0,1,0,-1},dy[4]={-1,0,1,0};
    cin >> H >> W >> Y >> X;
    X--;
    Y--;
    rep(i,0,H) cin >> S[i];
    int ans = 1;
    rep(i,0,4){
        int x=X, y=Y;
        while(1){
            x += dx[i];
            y += dy[i];

            if(x<0 || W<=x || y<0 || H<=y) break;
            if(S[y][x]=='#') break;
            ans++;
        }
    }
    cout << ans << endl;
}