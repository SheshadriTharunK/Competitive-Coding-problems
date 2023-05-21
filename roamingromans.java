import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a = scanner.nextDouble();
        double result =0.5+ (1000 * (5280.0 / 4854.0) * a);
        System.out.println((int)result);
    }
}