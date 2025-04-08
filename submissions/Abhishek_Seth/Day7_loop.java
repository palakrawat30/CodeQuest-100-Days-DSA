import java.util.*;
public class Day7_loop{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String n;
        int i;
        System.out.print("Enter the secret word: ");
        n=sc.nextLine();
        for (i = 0; i < 5; i++) {
            System.out.println(n);
        }
    }
}