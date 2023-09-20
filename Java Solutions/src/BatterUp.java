import java.util.Scanner;
public class BatterUp {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        in.nextLine();
        for (int time = 0; time < times; time++)
        {
            String input = in.nextLine();
            int index = input.indexOf(":");
            String name = input.substring(0, index);
            String batsstring = input.substring(index+1);
            String[] bats = batsstring.split(",");
            double points = 0;
            double atBats = bats.length;
            for (int i = 0; i < bats.length; i++)
            {
                if (bats[i].equals("3B")) points+=3;
                else if (bats[i].equals("2B")) points+=2;
                else if (bats[i].equals("1B")) points+=1;
                else if (bats[i].equals("HR")) points+=4;
                else if (bats[i].equals("BB")) atBats-=1;
            }
            System.out.printf("%s=%.3f%n", name, Math.round(points/atBats*1000.0)/1000.0);
        }
    }
}
