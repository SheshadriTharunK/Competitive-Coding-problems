import java.util.*;
public class triarea
{
    public static void main(String[] args){
   Scanner scanner=new Scanner(System.in);
   String a =scanner.nextLine();
   String[] numbers=a.split(" ");
   int b=Integer.parseInt(numbers[0]);
   int h=Integer.parseInt(numbers[1]);
   System.out.println(0.5*b*h);
    }
}

