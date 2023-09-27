import java.util.*;
public class likechecker
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int prev = -5;
        boolean check = true;
        while (n >= 10)
        {
            int curr = n % 10;
            if (curr <= prev)
            {
                System.out.println("No");
                check = false;
                break;
            }
            prev = curr;
            n /= 10;
        }
        if (n <= prev) 
        {
            System.out.println("No");
            check = false;
        }
        if (check == true) System.out.println("Yes");
        in.close();
    }
}