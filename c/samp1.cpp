#include <iostream>
#include <string>
using namespace std;

int main(){
  int x = -121;
  string y = to_string(x);
  for(int i=0;i<y.size();i++){
    if (y[i]==y[y.size()-(i+1)]){
      continue;
    }
    else{
    cout<<"false";
    break;
    }
  }
    cout<<"true";
}
