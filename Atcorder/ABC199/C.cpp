#include <bits/stdc++.h>
#define repr(i, n) for(int i = n; i >= 0; i--)
#define rep(i, m, n) for(int i = m; i < n; i++)
#define INF 2e9
#define ALL(v) v.begin(), v.end()
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
using namespace std;
typedef long long ll;
int main(){
    int N; string S; int Q;
    cin >> N >> S >> Q;
    string pre = S.substr(0,N);
    string post = S.substr(N);
    rep(i,0,Q){
        int T,A,B;
        cin >> T >> A >> B;
        if(T==1){
            A--;B--;
            if(B<N) swap(pre[A],pre[B]);
            else if(N<=A) swap(post[A-N], post[B-N]);
            else swap(pre[A], post[B-N]);
        }
        else{
            swap(pre,post);
        }
    }
    cout << pre << post << endl;
}