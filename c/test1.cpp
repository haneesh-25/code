#include <iostream>
using namespace std;

int main(){
  int one,two,three;
  three = 3;
  one = --three;
  three = 3;
  two = three--;
  cout<<"pre:"<<one<<" "<<"post:"<<two<<endl;
}
