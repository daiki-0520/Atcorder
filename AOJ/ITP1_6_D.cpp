#include <stdio.h>

using namespace std;

int main(){
    int n,m,tmp;
    scanf("%d %d",&n,&m);
    int A[n][m];
    int b[m];

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%d", &tmp);
            A[i][j] = tmp;
        }
    }
    for(int i=0; i<m; i++){
        scanf("%d",&tmp);
        b[i] = tmp;
    }
    long long sum;
    for(int i=0; i<n; i++){
        sum=0;
        for(int j=0; j<m; j++){
            sum += A[i][j] * b[j];
        }
        printf("%lld\n", sum);
    }
}