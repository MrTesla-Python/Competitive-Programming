import java.util.Scanner;
public class LookAfterThePennies
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            int transactions = in.nextInt();
            in.nextLine();
            double total = 0;
            for (int i = 0; i < transactions; i++)
            {
                double amount = in.nextDouble();
                in.nextLine();
                double rounded = Math.ceil(amount);
                total += rounded - amount;
                System.out.printf("%d%n", (int) rounded);
            }
            System.out.printf("%.2f%n", Math.round(total*100.0)/100.0);
        }
    }
}