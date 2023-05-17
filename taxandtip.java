import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
            Scanner scanner=new Scanner(System.in);
            int a =scanner.nextInt();
            double tax=0.18*a;
            double tip=0.05*a;
            double result=a+tax+tip;
            System.out.println(String.format("%.2f",result));
        
        
        
        
        
    }
}