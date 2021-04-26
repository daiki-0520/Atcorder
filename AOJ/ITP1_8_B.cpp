#include<iostream>
#include<string>
using namespace std;


int main(){
  string str;
  cin >> str;
  cout << typeid(str[0]).name();
  while(str[0]!='0'){
    int i,o=0;
    for(i=0;i<str.size();i++){
      o+=str[i]-'0';
    }
    cout << o << endl;
    cin >> str;
  }
  return 0;
}
