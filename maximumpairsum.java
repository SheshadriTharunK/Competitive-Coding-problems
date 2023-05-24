import java.io.*;
import java.util.*;
import java.util.Arrays;
public class Solution {

    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        int numbers[]=new int[n];
        for(int i=0;i<n;i++){
            numbers[i]=scanner.nextInt();
        }
        Arrays.sort(numbers);
        System.out.println(numbers[n-1]+numbers[n-2]);
        
        
        
    }
    
}