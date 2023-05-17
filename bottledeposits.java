import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
    Scanner scanner=new Scanner(System.in);
    String[]numbers = scanner.nextLine().split(" ");
    int number1=Integer.parseInt(numbers[0]);
    int number2=Integer.parseInt(numbers[1]);
    double result=number1*0.10+number2*0.25 ; 
    System.out.println(String.format("$%.2f",result));
        
        
        
        
        
    }
}