#include <iostream>
using namespace std;

int main(){
  int val;
  while (true){
    cout<<"enter value:";
    cin>>val;
    switch(val){
      case 0:
        cout<<"zero\n";
        break;
      default:
        if (val>0){
          cout<<"positive val\n";
        }
        else {
          cout<<"negative val\n";
        }
        break;
    }
  }
  return 0;
}
