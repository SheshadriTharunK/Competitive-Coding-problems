import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int numbers[]=new int[n];
        for (int i=0;i<n;i++){
            numbers[i]=sc.nextInt();
            
        }
        Arrays.sort(numbers);
        System.out.println(numbers[n-1]-numbers[0]);
        
    }
}