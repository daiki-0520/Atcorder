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
    int A,B;
    cin >> A >> B;
    int C=A+B;
    if (15<=C && 8<=B) cout << 1 << endl;
    else if(10<=C && 3<=B) cout << 2 << endl;
    else if(3<=C) cout << 3 << endl;
    else cout << 4 << endl;
    return 0;
}