import java.util.Scanner;
public class CaughtSpeeding {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            int speed = in.nextInt();
            boolean birthday = in.nextBoolean();
            int add_speed = 0;
            if (birthday) add_speed+=5;
            if (speed <= 60+add_speed) System.out.println("no ticket");
            else if (speed <= 80 + add_speed) System.out.println("small ticket");
            else System.out.println("big ticket");
        }
    }
}
