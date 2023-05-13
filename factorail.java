import java.util.Scanner; 
public class Main {
   static int factorial(int k)
   {
    if (k>0){
      return k*factorial(k-1);
      } 
    else {
      return 1;
   } 
   }
    public static void main(String[] args) 
    {
        Scanner scanner=new Scanner(System.in);
        int k=scanner.nextInt();
        int factorial=factorial(k);
        System.out.println(factorial); 
    }
    }