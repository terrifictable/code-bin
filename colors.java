public class colors {
  
  public static void main(String[] agrs) {
      
    for (int i=89; i<110; i++) {
    
      System.out.println(String.format("\033[%smTest", i) + String.format("  |  %s", i));
    }
  }
}
