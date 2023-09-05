public class list {
  public static void main(String[] args) {
    String myList[] = {"sam","rohit","vishnu","gowtham"};
    int inlist[] = {1,2,3,4,6};
    for(int i=0;i<10;i++){
      int raint = (int)(Math.random() * myList.length);
      System.out.println(myList[raint] + ' ' + raint);
    }
  }
}
