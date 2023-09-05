class some {
  private int age = 18;
  private String name = "rajiv";
  
  public void setAge(int newAge) {
    age = newAge;
  }
  public int getAge(){
    return age;
  }
  public String getName(){
    return name;
  }
}

public class encapsulating {
  public static void main(String[] args){
    some bio = new some();
    System.out.println(bio.getAge());
    bio.setAge(20);
    System.out.println(bio.getAge());
    System.out.println(bio.getName());
  }
}
