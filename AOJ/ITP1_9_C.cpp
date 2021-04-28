#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int t=0,h=0;
    string str1, str2;
    for(int i=0; i<n; i++){
        cin >> str1 >> str2;
        if(str1.compare(str2)==0){
            t++, h++;
        }else if(str1.compare(str2)>0) t+=3;
        else h+=3;
    }
    cout << t << " " << h << endl;
}