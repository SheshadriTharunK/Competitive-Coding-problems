'''TaxAndTip

Write a program that reads the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Compute the tax as 18 percent of the meal amount. Compute the tip as 5 percent of the meal amount (without the tax). Output the grand total for the meal including both the tax and the tip.

Input Format

A single line with a number - an integer representing the cost of a meal.

Constraints

Numbers will be in the range of 1 to 1000.

Output Format

Output a line with number representing the total cost. Format the output so that value is displayed using two decimal places.

Sample Input 0

100
Sample Output 0

123.00

 
1
​'''











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
