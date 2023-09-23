import java.util.Scanner;
public class AreWeOnABudget {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            int count = in.nextInt();
            in.nextLine();
            double [] budget = new double [count];
            double [] actual = new double [count];
            double total = 0;
            for (int i = 0; i < count; i++)
            {
                budget[i] = in.nextDouble();
            }
            in.nextLine();
            for (int i = 0; i < count; i++)
            {
                actual[i] = in.nextDouble();
                total += actual[i] - budget[i];
            }
            in.nextLine();
            System.out.printf("%.2f%n", total/count);
        }
    }
}
