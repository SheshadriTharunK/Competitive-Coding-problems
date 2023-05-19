import java.util.*;
public class pizza2{
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        String a=scanner.nextLine();
        String[] numbers=a.split(" ");
        int c=Integer.parseInt(numbers[0]);
        int r=Integer.parseInt(numbers[1]);
        double num=(c-r)*(c-r);
        double den=c*c;
        System.out.println((num/den)*100);
        }
    }
